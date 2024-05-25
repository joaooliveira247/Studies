import scala.io.StdIn.readInt


@main def ifElse(): Unit =
    println("Type a value")
    val userInput = readInt()
    if userInput < 0 then
        println("negative")
    else if userInput == 0 then
        println("zero")
    else
        if userInput > 10 then println("Grater than 10") else println("Positive")
        
