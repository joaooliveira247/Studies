package main

import "fmt"

func main() {
	arr := []int{1, 0, 3, 2, 0}
	fmt.Println(arr)
	fmt.Println(moveZeros(arr))
}

func moveZeros[T []int](arr T) T {
	buffer := 0
	for i := 0; i < len(arr); i++ {
		if arr[i] != 0 && arr[buffer] == 0 {
			arr[i], arr[buffer] = arr[buffer], arr[i]
		}

		if arr[buffer] != 0 {
			buffer++
		}
	}
	return arr
}
