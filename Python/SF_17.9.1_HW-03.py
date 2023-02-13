''' Напишите программу, которой на вход подается последовательность чисел через пробел,
    а также запрашивается у пользователя любое число.
    В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
    Далее программа работает по следующему алгоритму:
    1) Преобразование введённой последовательности в список
    2) Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
    3) Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
       а следующий за ним больше или равен этому числу.
    При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле.
    Реализуйте его также отдельной функцией.
    '''


def sort(array):
    # Решил воспользоваться своим придуманным алгоритмом сортировки, не стал брать готовые варианты.
    # Эффективность хуже, чем сортировка вставками, но оригинально.
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            sort(array)
            return array
    return array


def binary_search(array, element, left, right):
    if left > right:
        return f'Алгоритм поиска получил неожиданные входные данные\n{array}'
    middle = (right + left) // 2

    if array[0] < element < array[-1]:
        if array[middle - 1] < element <= array[middle]:
            return middle - 1
        elif element == array[middle - 1] and element == array[middle]:  # добавил, чтобы дубли корректно обходились
            return binary_search(array, element, left, middle - 1)
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    return 'Введённо число не удовлетворяет условиям поиска'


def start():
    try:
        arr = list(i for i in input('Введите целые числа через пробел: ').split())
        if not arr:
            raise ValueError
        int_arr = list(map(int, arr))
        element = int(input('Введите целое число: '))

        return binary_search(sort(int_arr), element, 0, len(int_arr) - 1)

    except ValueError or NameError as e:
        print('\nНеверные данные:\n - все поля должны быть заполнены\n'
              ' - можно вводить только целые числовые значения\n')
        return start()


print(start())