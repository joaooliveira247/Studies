package main

import "fmt"

// this example show how do it creating another slice
func main() {
	slice := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(removeEvenNumbersFromSlice(slice))
}

func removeEvenNumbersFromSlice(arr []int) (oddNumbers []int) {
	for idx, value := range arr {
		if value%2 != 0 {
			oddNumbers = append(oddNumbers, arr[idx])
		}
	}
	return
}
