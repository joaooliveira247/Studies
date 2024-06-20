package main

import (
	"fmt"
	"reflect"
)

func main() {
	var arr [5]int
	arr[0] = 1
	fmt.Println(arr)

	arr2 := [3]int{1, 2, 3}
	fmt.Println(arr2)

	arr3 := [...]int{1, 2, 3, 4, 5}
	fmt.Println(arr3)

	slice := []int{1, 2, 3, 4, 5}
	fmt.Println(slice)

	fmt.Println(reflect.TypeOf(arr3), reflect.TypeOf(slice))

	slice = append(slice, 19)
	fmt.Println(slice)

	slice2 := arr2[1:3]
	fmt.Println(slice2)

	// internal arrays

	slice3 := make([]float32, 10, 11)
	fmt.Println(slice3, len(slice3), cap(slice3))
	slice3 = append(slice3, 5, 6)
	fmt.Println(slice3, len(slice3), cap(slice3))
}
