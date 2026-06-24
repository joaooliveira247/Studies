package main

import "fmt"

func main() {
	// array
	arr := [3]int{1, 2, 3}

	fmt.Printf("Memory address of '%d': %p\n", arr[0], &arr[0])
	fmt.Printf("Memory address of '%d': %p\n", arr[1], &arr[1])
	fmt.Printf("Memory address of '%d': %p\n", arr[2], &arr[2])

	// slice
	slice := []int{1, 2, 3, 4}

	fmt.Printf("Memory address of slice '%d': %p\n", slice[0], &slice[0])
	fmt.Printf("Memory address of slice '%d' : %p\n", slice[1], &slice[1])
	fmt.Printf("Memory address of slice '%d': %p\n", slice[2], &slice[2])
	fmt.Printf("Memory address of slice '%d': %p\n", slice[3], &slice[3])
	slice = append(slice, 5)
	fmt.Printf("Memory address of slice '%d': %p\n", slice[4], &slice[4])
}
