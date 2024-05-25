import java.lang.ArithmeticException

@main def tryCatch(): Unit =
    try
        1 / 0
    catch 
        case ae: ArithmeticException => println("ArithmeticException")
    finally 
        println("Clean up your resources here.")