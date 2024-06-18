package main

import "fmt"

func main() {
	// int(host architeture), int8(byte), int16, int32(rune), int64, uint(unsigned)
	var intNum int16 = 100
	fmt.Println(intNum)
	// float32, float64
	var floatNum float32 = 56.32
	fmt.Println(floatNum)
	// string
	var text string = "Text"
	fmt.Println(text)
	// ascii value to char defined by ''
	char := 'a'
	fmt.Println(char)
	// empty values
	var name string
	fmt.Println(name)
	// bool - true, false
	var boolean bool = true
	fmt.Println(boolean)
	// error
	var err error
	fmt.Println(err)
}