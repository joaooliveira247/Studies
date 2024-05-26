class Person(var firstName: String, var lastName: String):
    def printFullName(): Unit = println(s"$firstName $lastName")


@main def classes(): Unit =
    val p = Person("John", "Stephens")
    println(p.firstName)
    p.lastName = "Legend"
    p.printFullName()