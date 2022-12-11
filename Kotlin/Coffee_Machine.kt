package machine

fun main() {
    /*println("Write how many ml of water the coffee machine has:")
    var water = readln().toInt()
    println("Write how many ml of milk the coffee machine has:")
    var milk = readln().toInt()
    println("Write how many grams of coffee beans the coffee machine has:")
    var beans = readln().toInt()
    println("Write how many cups of coffee you will need:")
    var cups = readln().toInt()*/

    val water: Int = 400
    val milk: Int = 540
    val beans: Int = 120
    val cupsDsp: Int = 9
    val money : Int = 550

    val listIngrid = mutableListOf(water, milk, beans, cupsDsp, money)

    menu(water, milk, beans, cupsDsp, money)

    /*if(cups * 200 > water || cups * 50 > milk || cups * 15 > beans) {
        println("No, I can make only ${cupsMax(water, milk, beans, cups = 0)} cups of coffee")
    } else if (cups * 200 <= water - 200 && cups * 50 <= milk - 50 && cups * 15 <= beans - 15) {
        println("Yes, I can make that amount of coffee (and even ${cupsMax(water, milk, beans, cups)} more than that)")
    } else println("Yes, I can make that amount of coffee")*/
}

fun menu(water: Int, milk: Int, beans: Int, cupsDsp: Int, money: Int) {
    println()
    println("Write action (buy, fill, take, remaining, exit):")
    val action = readln()
    if(action == "buy") buyAction(water, milk, beans, cupsDsp, money)
    if(action == "fill") fillAction(water, milk, beans, cupsDsp, money)
    if(action == "take") takeAction(water, milk, beans, cupsDsp, money)
    if(action == "remaining") amountIngrid(water, milk, beans, cupsDsp, money)
}

fun amountIngrid(water: Int, milk: Int, beans: Int, cupsDsp: Int, money: Int) {
    println()
    println("The coffee machine has:")
    println("$water ml of water")
    println("$milk ml of milk")
    println("$beans g of coffee beans")
    println("$cupsDsp disposable cups")
    println("$$money of money")
    menu(water, milk, beans, cupsDsp, money)
}

fun buyAction(water: Int, milk: Int, beans: Int, cupsDsp: Int, money: Int) {
    println()
    println("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
//    val listIngrid = mutableListOf(water, milk, beans, cupsDsp, money)
    when(readln().toString()) {
        "1" -> {
            if(water >= 250 && beans >= 16 && cupsDsp >= 1) {
                println("I have enough resources, making you a coffee!")
                menu(water - 250,      milk    , beans - 16, cupsDsp - 1, money + 4)
            } else if(water < 250) {
                println("Sorry, not enough water!")
                menu(water, milk, beans, cupsDsp, money)
            } else if(beans < 16) {
                println("Sorry, not enough beans!")
                menu(water, milk, beans, cupsDsp, money)
            } else if(cupsDsp < 1) {
                println("Sorry, not enough disposable cups!")
                menu(water, milk, beans, cupsDsp, money)
            }
        }
        "2" -> {
            if (water >= 350 && milk >= 75 && beans >= 20 && cupsDsp >= 1) {
                println("I have enough resources, making you a coffee!")
                menu(water - 350, milk - 75, beans - 20, cupsDsp - 1, money + 7)
            } else if (water < 350) {
                println("Sorry, not enough water!")
                menu(water, milk, beans, cupsDsp, money)
            } else if (milk < 75) {
                println("Sorry, not enough milk!")
                menu(water, milk, beans, cupsDsp, money)
            } else if (beans < 20) {
                println("Sorry, not enough beans!")
                menu(water, milk, beans, cupsDsp, money)
            } else if (cupsDsp < 1) {
                println("Sorry, not enough disposable cups!")
                menu(water, milk, beans, cupsDsp, money)
            }
        }
        "3" -> {
            if (water >= 200 && milk >= 100 && beans >= 12 && cupsDsp >= 1) {
                println("I have enough resources, making you a coffee!")
                menu(water - 200, milk - 100, beans - 12, cupsDsp - 1, money + 6)
            } else if (water < 200) {
                println("Sorry, not enough water!")
                menu(water, milk, beans, cupsDsp, money)
            } else if (milk < 100) {
                println("Sorry, not enough milk!")
                menu(water, milk, beans, cupsDsp, money)
            } else if (beans < 12) {
                println("Sorry, not enough beans!")
                menu(water, milk, beans, cupsDsp, money)
            } else if (cupsDsp < 1) {
                println("Sorry, not enough disposable cups!")
                menu(water, milk, beans, cupsDsp, money)
            }
        }
        "back" -> menu(water, milk, beans, cupsDsp, money)
    }
}

fun fillAction(water: Int, milk: Int, beans: Int, cupsDsp: Int, money: Int) {
    println()
    val listIngrid = mutableListOf(water, milk, beans, cupsDsp, money)
    println("Write how many ml of water you want to add:")
    listIngrid[0] += readln().toInt()
    println("Write how many ml of milk you want to add:")
    listIngrid[1] += readln().toInt()
    println("Write how many grams of coffee beans you want to add:")
    listIngrid[2] += readln().toInt()
    println("Write how many disposable cups you want to add: ")
    listIngrid[3] += readln().toInt()
    menu(listIngrid[0], listIngrid[1], listIngrid[2], listIngrid[3], listIngrid[4])
}

fun takeAction(water: Int, milk: Int, beans: Int, cupsDsp: Int, money: Int) {
    println()
    println("I gave you $$money")
    menu(water, milk, beans, cupsDsp, 0)
}

fun cupsMax(water: Int, milk: Int, beans: Int, cups: Int): Int {
    val cupsMax: Int
    val list = mutableListOf<Int>()
    list.add((water - 200 * cups) / 200)
    list.add((milk - 50 * cups) / 50)
    list.add((beans - 15 * cups) / 15)
    cupsMax = list.minOrNull()!!.toInt()
    return cupsMax
}

fun ingredients() {
    println("Write how many cups of coffee you will need:")
    val cups = readln().toInt()
    println("For 125 cups of coffee you will need:")
    println("${cups * 200} ml of water")
    println("${cups * 50} ml of milk")
    println("${cups * 15} g of coffee beans")
}

fun firstPrint() {
    println("Starting to make a coffee")
    println("Grinding coffee beans")
    println("Boiling water")
    println("Mixing boiled water with crushed coffee beans")
    println("Pouring coffee into the cup")
    println("Pouring some milk into the cup")
    println("Coffee is ready!")
}
