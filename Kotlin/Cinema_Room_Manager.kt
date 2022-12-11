import kotlin.system.exitProcess

fun main() {
    println("Enter the number of rows:")
    val numberOfRows = readln().toInt()

    println("Enter the number of seats in each row:")
    val numberOfSeats = readln().toInt()

    val hall = MutableList(numberOfRows) { MutableList(numberOfSeats) { "S" } }

    println()
    menu(numberOfRows, numberOfSeats, hall)
}
fun Statistics(hall: MutableList<MutableList<String>>, numberOfRows: Int, numberOfSeats: Int) {
    var buyCount = 0
    for (i in hall) {
        buyCount += i.count{it == "B"}
    }
    println("Number of purchased tickets: $buyCount")
    var percent = buyCount.toFloat() / (numberOfRows * numberOfSeats) * 100
    println("Percentage: " + "%.2f".format(percent) + "%")

    var price = 0
    if (numberOfRows * numberOfSeats <= 60) {
        println("Current income: \$${buyCount * 10}")
    } else {
        for (i in hall.indices) {
            if ((i + 1) <= numberOfRows / 2) {
                hall[i].forEach{if (it == "B") price += 10}
            }  else hall[i].forEach{if (it == "B") price += 8}
        }
        println("Current income: \$$price")
    }
    totalIncomPrint(numberOfRows, numberOfSeats)
    println()
    menu(numberOfRows, numberOfSeats, hall)
}

fun buyTicket(numberOfRows: Int, numberOfSeats: Int, hall: MutableList<MutableList<String>>) {
    println()
    println("Enter a row number:")
    val row = readln().toInt()
    println("Enter a seat number in that row:")
    val seat = readln().toInt()
    if ((row - 1) < numberOfRows && (seat - 1) < numberOfSeats) {
        if (hall[row - 1][seat - 1] == "S") {
            hall[row - 1][seat - 1] = "B"
            pricePrint(numberOfRows, numberOfSeats, row, hall)
            menu(numberOfRows, numberOfSeats, hall)
        } else {
            println("That ticket has already been purchased!")
            buyTicket(numberOfRows, numberOfSeats, hall)
        }
    } else {
        println("Wrong input!")
        buyTicket(numberOfRows, numberOfSeats, hall)
    }
}

fun hallPrint(numberOfRows: Int, numberOfSeats: Int, hall: MutableList<MutableList<String>>) {
    println()
    println("Cinema:")
    print("  ")
    var n = 1
    while (n < numberOfSeats) {
        print("$n ")
        n++
    }
    println(n)
    n = 1
    for (i in hall) {
        print("$n ")
        println(i.joinToString(" "))
        n++
    }
    println()
    menu(numberOfRows, numberOfSeats, hall)
}

fun totalIncomPrint(numberOfRows: Int, numberOfSeats: Int) {
    val totalIncom: Int
    if (numberOfRows * numberOfSeats <= 60) {
        totalIncom = numberOfRows * numberOfSeats * 10
    } else {
        totalIncom = (numberOfRows / 2) * numberOfSeats * 10 + (numberOfRows - numberOfRows / 2) * numberOfSeats * 8
    }
    println("Total income: \$$totalIncom")
    println()
}

fun pricePrint(numberOfRows: Int, numberOfSeats: Int, row: Int, hall: MutableList<MutableList<String>>) {
    println()
    val price: Int
    if (numberOfRows * numberOfSeats <= 60) {
        price = 10
    } else if (row <= numberOfRows / 2){
        price = 10
    } else price = 8
    println("Ticket price: \$$price")
    println()
    menu(numberOfRows, numberOfSeats, hall)
}

fun menu(numberOfRows: Int, numberOfSeats: Int, hall: MutableList<MutableList<String>>) {
    println("1. Show the seats\n2. Buy a ticket\n3. Statistics\n0. Exit")
    println()
    val input = readln().toInt()
    if (input == 1) {
        return hallPrint(numberOfRows, numberOfSeats, hall)
    } else if (input == 2) {
        return buyTicket(numberOfRows, numberOfSeats, hall)
    } else if (input == 3) {
        return Statistics(hall, numberOfRows, numberOfSeats)
    } else exitProcess(0)
}