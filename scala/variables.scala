@main def variables(): Unit =
    val msg: String = "Hello immutable"
    // msg = "Something" this is not muttable
    println(msg)
    var msg_2: String = "Hello World"
    println(msg_2)
    msg_2 = "Hello Mutable Var"
    println(msg_2)