import scala.math.*

// Utility Objects
object StringUtils:
    def isNullOrEmpty(s: String): Boolean = s == null || s.trim.isEmpty()
    def leftTrim(s: String): String = s.replaceAll("^\\s+", "")
    def rightTrim(s: String): String = s.replaceAll("\\s+$", "")


// Companion objects
class Circle(radius: Double):
    import Circle.*
    // companion objects can acess provate methods in objects
    def area: Double = calculateArea(radius)


object Circle:
    private def calculateArea(radius: Double): Double =
        Pi * pow(radius, 2.0)


// Creating modules from traits
trait AddService:
    def add(a: Int, b: Int): Int = a + b


trait MultiplyService:
    def multiply(a: Int, b: Int): Int = a * b


object MathService extends AddService, MultiplyService

@main def singleton(): Unit =
    import MathService.*
    println(StringUtils.isNullOrEmpty(""))
    println(StringUtils.isNullOrEmpty("a"))
    val circle1 = Circle(5.0)
    println(circle1.area)
    println(add(1, 1))
    println(multiply(2, 2))
