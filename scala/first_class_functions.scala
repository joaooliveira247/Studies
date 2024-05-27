def double(i: Int): Int = i * 2

@main def firstClassFunctions(): Unit =
    val a = List(1, 2, 3).map(i => i * 2)
    val b = List(1, 2, 3).map(_ * 2)
    println(s"$a, $b")
    val a2 = List(1, 2, 3).map(i => double(i))
    val b2 = List(1, 2, 3).map(double)
    println(s"$a2, $b2")
    // immutable collections List, Vector, Map, Set
    val nums = (1 to 10).toList

    val x = nums.filter(_ > 3)
                .filter(_ < 7)
                .map(_ * 10)
    println(s"$nums, $x")