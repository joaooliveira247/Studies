@main def lists(): Unit =
    val a = List(1, 2, 3)

    // With range
    val b = (1 to 5).toList
    val c = (1 to 10 by 2).toList
    val e = (1 until 5).toList
    val f = List.range(1,5)
    val g = List.range(1, 10, 3)
    val h = List()
    println(s"$a,$b,$c,,$e,$f,$g,$h")

    val example = List(10, 20, 30, 40, 10)
    println(example)
    println(example.drop(2))
    println(example.dropWhile(_ < 25))
    println(example.filter(_ < 25))
    println(example.slice(2, 4))
    println(example.tail)
    println(example.take(3))
    println(example.takeWhile(_ < 30))

    // flatten

    val example2 = List(List(1, 2), List(1, 2))
    println(example2.flatten)

    // map, flatMap
    val nums = List("One", "Two")
    println(nums.map(_.toUpperCase))
    println(nums.flatMap(_.toUpperCase))

    // foldLeft and ReduceLeft only for integers
    val firstTen = (1 to 10).toList

    println(firstTen.reduceLeft(_ + _))
    println(firstTen.foldLeft(100)(_ + _))


        