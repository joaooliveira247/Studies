package main

import "fmt"

type User struct {
	Name string
}

func main() {
	// zero values
	var zInt int
	var zFloat float32
	var zString string
	var zStruct User
	var zMap map[string]int
	var zSlice []int

	fmt.Println(zInt, zFloat, zString, zStruct, zMap, zSlice)

	x := 100

	// pointer to x (address to x) y address is different to x
	y := &x

	// * is used to mark something as pointer or deref
	fmt.Println(x, y, *y)

	// =======================================================================

	stringValue := "Hello"

	// here original value of string
	fmt.Println(stringValue)

	// here take a copy and change only copy
	takeStringCopy(stringValue)

	fmt.Println(stringValue)

	// here function change value of string
	changeStringRef(&stringValue)

	fmt.Println(stringValue)
}

func takeStringCopy(value string) {
	value = "takeStringCopy"
	fmt.Println(value)
}

func changeStringRef(value *string) {
	*value = "changeStringRef"
	fmt.Println(*value)
}
