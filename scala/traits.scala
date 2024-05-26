trait Speaker:
    def speak(): String


trait TailWagger:
    def startTrail: Unit = println("tail is wagging")
    def stopTrail: Unit = println("tail is stopped")


trait Runner:
    def startRunning(): Unit = println("I'm running")
    def stopRunning(): Unit = println("Stopped running")


class Dog(name: String) extends Speaker, TailWagger, Runner:
    def speak(): String = "Woof"


class Cat(name: String) extends Speaker, TailWagger, Runner:
    def speak(): String = "Meow"
    override def startRunning(): Unit = println("Yeah ... I don't run")
    override def stopRunning(): Unit = println("No need to stop")


@main def traits(): Unit =
    val d = Dog("Rover")
    println(d.speak())

    val c = Cat("Morris")
    println(c.speak())
    c.startRunning()
    c.stopRunning()