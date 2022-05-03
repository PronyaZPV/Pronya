// Дан файл с массивов объектов JSON. Каждый объект является идентификационной карточкой человека. 
// Нам нужно хранить только уникальные значения в этом массиве. Реализуйте функцию, которая будет выполнять эту работу.

const fs = require('fs')                    // загружаем модуль fs 
let file = fs.readFileSync('JS. HW_3 task2.json')    // получаем данные из файла (в скобках относительный путь к файлу) в шестнадцатеричном виде
let personFile = JSON.parse(file)           // переводим шестнадцатеричные данные в JSON

function person (person) {
    for (i = 0; i < person.length - 1; i++) {             // делаю цикл, который будет перебирать элементы и одновременно сравнивать
        for (i2 = person.length - 1; i2 > i; i2--) {      // вложенный цикл для встречного перебора элементов в массиве с конца
            if (person[i].username == person[i2].username && person[i].email == person[i2].email) {   // сравниваю 'username' и 'email', если они равны, то удаляю элемент, который ближе к концу списка
                person.splice(i2,1)
            }
        }
    }

    for (k1 = 0; k1 < person.length; k1++) {               // вывожу для визуальной проверки итоговый список людей
        console.log(person[k1].name, person[k1].username)
    }
}

person(personFile)