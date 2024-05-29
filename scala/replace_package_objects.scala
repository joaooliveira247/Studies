package foo {
    def double(i: Int): Int = i * 2
}

package foo {
    package bar {
        @main def foorBarMain =
            println(s"${double(1)}")
    }
}