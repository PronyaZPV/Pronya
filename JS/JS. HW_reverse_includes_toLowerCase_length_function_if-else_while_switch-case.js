// // Написать скриптик, который сосчитает и выведет результат от возведения 2 в степень 10, начиная со степени 1
// let a = 1 
// let res = 2
// while (a < 10) {
//     res = res * 2
//     a++
// } console.log(res)


//  // Преобразовать 1 задачу в функцию, принимающую на вход число и степень, в которую будет возводиться число
// function step(a, step) {
//     let res = a
//     for (let i = 1; i < step; i++) {
//         res = res * a
//     } 
//     console.log(res)
// }
// step(3,7)


//  // Написать скрипт, который выведет 5 строк в консоль таким образом, чтобы в первой строчке выводилось :), во второй :):) и так далее'.
//  // Преобразовать в функцию, принимающую на вход строку, которая и будет выводиться в консоль (как в условии смайлик), а также количество строк для вывода
// function smile(stroka, numberOfRows) {
//     let i = 1
//     res = stroka
//     while (i <= numberOfRows) {
//         console.log(res)
//         res = res + stroka        
//         i++
//     }
// }
// smile('||', 7)


// Написать функцию, которая принимает на вход слово. Задача функции посчитать и вывести в консоль, сколько в слове гласных, и сколько согласных букв.
function word(word) {
    let leters = Array.from(word) 
    glasnyRes = 0
    soglasnRes = 0
    let glasny = 'eyuioa'.split('')
    let soglas = 'qwrtpsdfghjklzxcvbnm'.split('')

    for (let i = 0; i < leters.length; i++) {
        if (glasny.includes(leters[i].toLowerCase())) 
            glasnyRes++
        else if (soglas.includes(leters[i].toLowerCase())) 
            soglasnRes++
    }
    console.log('Слово "' + word + '" состоит из ' + glasnyRes + ' гласных и ' + soglasnRes + ' согласных букв')
}
word('Check-list')
word('Case')
word('case')


// Написать функцию, которая проверяет, является ли слово палиндромом
function isPalindrom(word) {
    let revers = word.split('').reverse().join('')
    if (word.toLowerCase() == revers.toLowerCase())
        console.log ('Слово - полиндром')
    else
        console.log ('Слово - НЕ полиндром')
}
isPalindrom('Abba')
isPalindrom('abba')
isPalindrom('sAbba')

// // switch-case
// function age(age) {
//     switch (age) {
//         case 17:
//             console.log('small')
//             break
//         case 18:
//             console.log('norm')
//             break
//         case 70:
//             console.log('old')
//             break
//         default:
//             console.log('what!?')
//     }
// }

// age(17)
// age(18)
// age(59)
// age(70)
// age('big')

