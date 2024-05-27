import java.io.StringWriter
import java.io.PrintWriter

def sum(a: Int, b: Int): Int = a + b

def concat(s1: String, s2: String): String = s"$s1$s2"

def getStackTraceAsString(t: Throwable): String =
    val sw = new StringWriter
    t.printStackTrace(new PrintWriter(sw))
    sw.toString()

def makeConnection(url: String, timeout: Int = 5000): Unit =
    println(s"url=$url, timeout=$timeout")

extension (s: String)
    def makeInt(radix: Int): Int = Integer.parseInt(s, radix)

@main def methods(): Unit =
    println(sum(1, 2))
    println(concat("foo ", "bar"))
    makeConnection("https://localhost")
    "1".makeInt(2)
    "10".makeInt(2)
