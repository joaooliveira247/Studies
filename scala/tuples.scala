case class Person2(name: String)

@main def tuples(): Unit =
    val t = (11, "eleven", Person2("Eleven"))
    println(t)
    println(s"${t(0)}, ${t(1)}, ${t(2)}")

    val (num, str, person) = t
    println(s"$num $str $person")