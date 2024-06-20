package main

import "fmt"

func weekDay(num int) string {
	switch num {
	case 1:
		return "Sunday"
	case 2:
		return "Monday"
	case 3:
		return "Tuesday"
	case 4:
		return "Wednesday"
	case 5:
		return "Thursday"
	case 6:
		return "Friday"
	case 7:
		return "Saturday"
	default:
		return "Option not found"
	}
}

func main() {
	day := 3
	fmt.Println(weekDay(day), weekDay(4), weekDay(200))
}