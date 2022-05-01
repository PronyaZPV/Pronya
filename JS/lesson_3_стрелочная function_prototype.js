function yolochka1() {  // пустая функция, будет работать без переменной
    let mass = 'Hello_1'
    console.log(mass)
} yolochka1()


// ниже то же самое, но в виде стрелочной функции
let yolochka2 = () => {let mass2 = 'Hello_2'; console.log(mass2)}
yolochka2()

let f22 = (t11, t22) => {console.log('Sum ' + t11 + t22)}
f22(5, 6)


// ниже стрелочная функция, где на вызове функции вставляются переменные
let t1 = 30
let t2 = 20

let t3 = 30
let t4 = 40

let f33 = (t1 > t2) ? 
    (tt1, tt2) => console.log('order ', tt1 + tt2) : 
    (tt1, tt2) => console.log('order ', tt1 - tt2)

f33(t3, t4) // из этих переменных берутся tt1 / tt2


// прототипы - создание своих методов/свойств
function yolochka33(){}

yolochka33.prototype.fast = function(){
    console.log('FAST!!')
}

yolochka33.prototype.green = function(sun, co2){
    console.log('Green == ', sun,  ' + ',  co2)
}

yolochka33.prototype.shishki = function (){
    console.log('shishki == yolki')
}

let forest = new yolochka33()

forest.fast()
forest.green(4500, 50)
forest.shishki()