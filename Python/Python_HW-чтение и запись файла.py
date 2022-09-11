''' Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Раскодировать a3b4c2e10b1 в aaabbbbcceeeeeeeeeeb'''
# Моя хрень:
with open('dataset.txt') as inf:
    s = inf.readline().strip()
#s = 'a3b4c2ev10b1'
list = [s[0]]
for i in range(len(s)-1):
    i += 1  
    if list[-1].isalpha() and s[i].isdigit():
        list.append(s[i])   
    elif list[-1].isdigit() and s[i].isalpha():
        list.append(s[i]) 
    elif list[-1].isdigit() and s[i].isdigit():
        list[-1] += s[i]       
        i+=1       
res = ''
for i in range(len(list)-1):
    if list[i].isalpha():
        l = list[i]*(int(list[i+1]))
        res += l
with open("dataset.txt", 'w') as inf_out:
    inf_out.write(res)

# норм:
with open('dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()
i = 0
while i < len(s):
    j = i + 1
    while j < len(s) and s[j].isdigit():
        j += 1
    print(s[i] * int(s[i+1:j]), end='')
    i = j

#--------------------
m, s, n = '', '', 0
with open('dataset_3363_2.txt', 'r+') as f:     # открываем файл в режиме чтение и запись
    for i in f.readline():                      # читаем строку и перебираем
        if '0' <= i <= '9':                     # если число
            n += i                              # соединяем числа в строку
            continue
        m += s * int(n)                         # преобразуем число в соответствующее количество символов
        s, n = i, ''
    f.seek(0)                                   # перемещаем указатель в начало файла для перезаписи
    f.write(m)  

# с помощью регулярки
import re
with open("dataset_3363_2.txt", "r") as file:
    s = file.read()
print("".join(c * int(n_str) for c, n_str in re.findall(r"(\w)(\d+)", s)))

''' Решение с использованием модуля re, regular expressions. Этот модуль позволяет декодировать строку вызовом одной функции re.sub(pattern, replace, string). 
В качестве replace можно передавать или функцию (как у меня в решении) или строку.'''
import re

def repl(m):
    return m.group(1) * int(m.group(2))

with open('input.txt', 'r') as data:
    s = data.read()
    s = s.rstrip()

pattern = r'(\w)(\d+)'
s = re.sub(pattern, repl, s)

with open('output.txt', 'w') as data:
    data.write(s)


''' Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. 
Если таких слов несколько, вывести лексикографически первое. В качестве ответа укажите вывод программы, а не саму программу. Слова, написанные в разных регистрах, считаются одинаковыми.
Пример: abc a bCd bC AbC BC BCD bcd ABC  -->  abc 3'''

from typing import Counter
with open('dataset.txt', encoding='utf-8') as inf:
    arr = inf.read().replace('\n', '\x20').lower().split()  # считал все строки, заменил перенос строки на пробел, уменьшил регистр букв, разбил на список по пробелам

d = dict(Counter(arr))      # посчитал совпадения значений {key:value} и сменили тип получившегося объекта на тип - словарь
max_value = d[max(d, key = lambda k: d[k])]     # выяснил макимальное value в словаре
res_d = d.copy()
for i in d:  
    if d[i] != max_value:
        del res_d[i]                            # сделал новый словарь, удалив все ключи с не максимальным значением
res = min(res_d) + '\x20' + str(max_value)      # через пробел прописал ответ

with open("dataset.txt", 'w', encoding='utf-8') as inf:
    inf.write(res)




#-----------------------
with open('words.txt') as f:
    text = f.read().lower().split()
popular_word = max(set(text), key=text.count)
print(popular_word, text.count(popular_word))

#-----------------------
with open('dataset.txt', 'r') as x:
    x = "".join(s.readlines()).split()
m = max([x.count(f) for f in x])
t = [g for g in x if x.count(g) == m][0]
print(t, m)


''' Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку. Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.
Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные значения, разделённые пробелом, последней строкой в файл с ответом.
Петров;85;92;78         85.0
Сидоров;100;88;94 --->  94.0
Иванов;58;72;85         71.666666667
                        81.0 84.0 85.666666667
'''
with open('dataset.txt', encoding='utf-8') as inf:
    arr = []
    arr = inf.read().split('\n')        # считал весь текст, разбив строки на список
    arr = [i.split(';') for i in arr]   # разбил строки в списке на списки с разделением по ;
    int_arr = [[int(i) if i.isdigit() else i for i in j] for j in arr]  # преобразовал числа в формат int
    
    avg_student = ''
    for i in int_arr:                               # посчитал среднее по студентам
        avg_student += (str(sum(i[1:])/3))+'\n'
    
    avg_res = []                                    # посчитал среднее по предметам
    for j in range(1,4):
        s=0
        for i in int_arr:
            s += i[j]/len(int_arr)   
        avg_res.append(s)

with open("dataset.txt", 'w') as inf:
    inf.write(avg_student + ' '.join(map(str, avg_res)))    # вывел в файл в нужном формате


''' На вхоже файл, в котором ссылка на скачивание другого файла. Нужно на выходе получить кол-во строк текста в том файле.
Решить с помощью requests '''
import requests
with open ('dataset.txt') as inf:
    url = inf.readline().strip()
print(len(requests.get(url).text.splitlines()))     # разбил текст на список построчно, вывел кол-во элементов списка