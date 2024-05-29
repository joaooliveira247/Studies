import scala.collection.mutable.ArrayBuffer

enum Topping2:
    case Cheese, Pepperoni, Mushrooms

import Topping2.*
class Pizza:
    val toppings = ArrayBuffer[Topping2]()

val p = Pizza()

extension (s: String)
    def capitalizaAllWords = s.split(" ").map(_.capitalize).mkString(" ")

val hwUpper = "hello, world".capitalizaAllWords

type Money = BigDecimal

@main def myApp =
    p.toppings += Cheese
    println("Show me the code".capitalizaAllWords)
