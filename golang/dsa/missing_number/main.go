package main

import "fmt"

func missingNumber(nums []int) int {
	arrLenght := len(nums)
	sum := arrLenght * (arrLenght + 1) / 2

	for _, value := range nums {
		sum -= value
	}

	return sum
}

func main() {
	arr := []int{0, 1, 3}
	fmt.Println(missingNumber(arr))
}
