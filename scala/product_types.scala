case class Person_2(
    name: String,
    vocation: String
)

@main def productTypes(): Unit =
    // fields in case class are immutables
    val p = Person_2("Reginald Kenneth Dwight", "Singer")

    println(p)
    println(p.name)
    // p.name = "Joe"
    val p2 = p.copy(name = "Elton John")
    println(p2)
