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

	item := s.items[len(s.items)-1]
	s.items = s.items[:len(s.items)-1]
	return item
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

func isValid(s string) bool {
	var stack Stack[rune]

	for _, char := range s {
		switch char {
		case '(', '{', '[':
			stack.push(char)
		default:
			if stack.isEmpty() {
				return false
			}

			top := stack.peek()

			if (char == ')' && top == '(') ||
				(char == '}' && top == '{') ||
				(char == ']' && top == '[') {
				stack.pop()
			} else {
				return false
			}
		}
	}
	return true
}

func main() {
	fmt.Println(isValid("()"))
	fmt.Println(isValid("{{()}}"))
	fmt.Println(isValid("{{(()}}"))
}
