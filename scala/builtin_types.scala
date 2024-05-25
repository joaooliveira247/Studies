@main def builtIn(): Unit =
    val b: Byte = 1
    val i: Int = 1
    val l: Long = 1
    val s: Short = 1
    val x = 1_000L // Long
    val y = 2.2D // Double
    val z = 3.3F // Float
    var a = BigInt(1_234_567_890_987_654_321L)
    var big_d = BigDecimal(123_456.789)
    val name: String = "Bill"
    val c: Char = 'a'

    // format string
    val firstName = "John"
    val mi = 'C'
    val lastName = "Doe"

    println(s"Name: $firstName $mi $lastName")

    println(s"2 + 2 = ${2 + 2}")

    val x_abs = -1
    println(s"x.abs = ${x_abs.abs}")

    // Multiline string
    val quote = """The essence of Scala:
               Fusion of functional and object-oriented
               programming in a typed setting."""

    println(quote)