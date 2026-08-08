package main

import "fmt"

type Stack[T any] struct {
	items []T
}

func (s *Stack[T]) push(item T) {
	s.items = append(s.items, item)
}

func (s *Stack[T]) pop() T {
	if len(s.items) == 0 {
		var zero T
		return zero
	}
	result := s.items[len(s.items)-1]
	s.items = s.items[:len(s.items)-1]
	return result
}

func (s *Stack[T]) peek() T {
	if len(s.items) == 0 {
		var zero T
		return zero
	}
	return s.items[len(s.items)-1]
}

func (s *Stack[T]) isEmpty() bool {
	return len(s.items) == 0
}

func nextGreaterElement[U int](arr []U) []U {
	n := len(arr)
	res := make([]U, n)
	var stack Stack[U]

	for i := n - 1; i >= 0; i-- {
		if !stack.isEmpty() {
			for !stack.isEmpty() && stack.peek() <= arr[i] {
				stack.pop()
			}
		}

		if stack.isEmpty() {
			res[i] = -1
		} else {
			res[i] = stack.peek()
		}

		stack.push(arr[i])
	}
	return res
}

func main() {
	fmt.Println(nextGreaterElement([]int{1, 2, 3, 4, 5}))
}
