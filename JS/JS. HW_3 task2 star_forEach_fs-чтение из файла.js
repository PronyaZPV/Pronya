// Дан файл с массивов объектов JSON. Каждый объект является идентификационной карточкой человека. 
// Нам нужно хранить только уникальные значения в этом массиве. Реализуйте функцию, которая будет выполнять эту работу.

const fs = require('fs')                    // загружаем модуль fs 
let file = fs.readFileSync('JS. HW_3 task2.json')    // получаем данные из файла (в скобках относительный путь к файлу) в шестнадцатеричном виде
let personFile = JSON.parse(file)           // переводим шестнадцатеричные данные в JSON

function person (person) {
    person.forEach ((user,m) => {             // для каждого элемента user и его порядкового номера m из массива
        for (i = person.length - 1; i > m; i--) {      // вложенный цикл для встречного перебора элементов в массиве с конца
            if (user.username == person[i].username && user.email == person[i].email) {   // сравниваю 'username' и 'email', если они равны, то удаляю элемент, который ближе к концу списка
                person.splice(i,1)
            }
        }
    })

    for (n = 0; n < person.length; n++) {               // вывожу для визуальной проверки итоговый список людей
        console.log(person[n].name, person[n].username)
    }
}

person(personFile)