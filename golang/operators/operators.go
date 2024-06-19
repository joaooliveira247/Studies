package main

import "fmt"

func main() {
	// arithmetic (+, -, *, /, %)
	arithmetic := fmt.Sprintf(
		"1 + 1 = %d, 3 - 2 = %d, 3 * 2 = %d, 3 / 3 = %d, 5 %% 2 = %d",
		1+1,
		3-2,
		3*2,
		3/3,
		5%2,
	)
	fmt.Println(arithmetic)
	fmt.Println(5 % 2)
	// atribuition (=, :=)
	var text string = "text"
	someName := "someOne"
	fmt.Println(text, someName)
	// retalional (==, !=, >, <, >=, <=)
	relational := fmt.Sprintf(
		"1 == 1 = %t, 1 != 2 = %t, 1 > 2 = %t, 1 < 2 = %t, 1 >= 1 = %t, 3 <= 5 %t",
		1 == 1, 1 != 2, 1 > 2, 1 < 2, 1 >= 1, 3 <= 5,
	)
	fmt.Println(relational)
	// logical
	logical := fmt.Sprintf(
		"AND(&&) true && true = %t, OR(||) true || false = %t, NOT(!) !true =%t",
		true && true, true || false, !true,
	)
	fmt.Println(logical)

	var num int8 = 6
	num++
	num += 10
	fmt.Println(num)
}
