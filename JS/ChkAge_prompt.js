// проверка возраста в браузере, вывод в консоль. 
// Таким образом, чтобы первым делом в функции проверялся тип данных. И если он не Number - кидалась ошибка.
// Таким образом, чтобы значение '2' (строка в которой лежит ТОЛЬКО ЦИФРА) пропускалось, преобразовываясь в number
// Таким образом, чтобы возраст вводится используя функцию prompt в привязанной верстке

const chkAge = function(age) {
    // age = Number(age) - в number необязательно переводить, т.к. isNaN так и так переводит в number
    if (!isNaN(age)) {
    // if (Number(age)) тоже будет работать, т.к. Number всегда возвращает number(а число = True) или NaN (оно всегда = False)
    // if (+age)    то же самое как Number(age)
        if (typeof(age) == 'number') {
            if (age < 18)
                console.log("You don`t have access cause your age is " + age + " It`s less then 18")

            else if (age >= 18 && age <= 60) 
                    console.log("Welcome  !")

            else if (age > 60) 
                    console.log("Keep calm and look Culture channel")
                
            else console.log("Technical work")
            }
    }
    else console.log("Error. Enter a number")
}

chkAge(17)
chkAge(35)

let agePrompt = prompt("Enter age", [''])
chkAge(agePrompt)
