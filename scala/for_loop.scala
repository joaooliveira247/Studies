import scala.compiletime.ops.double
@main def forLoop(): Unit =
    val ints = List(1, 2, 3, 4, 5)
    for i <- ints do println(i)

    // guards
    for
        i <- ints
        if i > 2
    do
        println(i)

    // range

    for
        i <- 1 to 3
        j <- 'a' to 'c'
        if i == 2
        if j == 'b'
    do
        println(s"i = $i, j = $j")

    // for expressions, like python comprehensions

    val doubles = for i <- ints yield i * 2
    println(doubles)

    val names = List("chris", "ed", "maurice")
    val capNames = for name <- names yield name.capitalize
    println(capNames)

    val fruits = List("apple", "banana", "lime", "orange")

    val fruitLengths = for 
        f <- fruits
        if f.length > 4
    yield
        f.length
    println(fruitLengths)