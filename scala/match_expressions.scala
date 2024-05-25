import scala.compiletime.ops.string
def getClassAsString(x: Matchable): String = x match
    case s: String => s"'$s' is a String"
    case i: Int => "Int"
    case d: Double => "Double"
    case l: List[?] => "List"
    case _ => "Unknown"


@main def matchExpression(): Unit =
    val i = 1

    i match
        case 1 => println("One")
        case 2 => println("Two")
        case _ => println(s"Other ($i)")
    
    println(getClassAsString(1))
    println(getClassAsString("Hello"))
    println(getClassAsString(List(1, 2, 3)))