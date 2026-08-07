package main

import (
	"fmt"
	"strings"
)

type Stack struct {
	items []string
}

func (s Stack) String() string {
	if len(s.items) == 0 {
		return "[ ] (empty stack)"
	}

	maxLen := 0
	for _, item := range s.items {
		if len(item) > maxLen {
			maxLen = len(item)
		}
	}

	var sb strings.Builder

	sb.WriteString("┌" + strings.Repeat(" ", maxLen+2) + "┐\n")

	for i := len(s.items) - 1; i >= 0; i-- {
		itemFormatted := fmt.Sprintf("│ %-*s │\n", maxLen, s.items[i])
		sb.WriteString(itemFormatted)
	}

	sb.WriteString("└" + strings.Repeat("─", maxLen+2) + "┘")

	return sb.String()

}

func (s *Stack) push(item string) {
	s.items = append(s.items, item)
}

func (s *Stack) pop() string {
	if len(s.items) == 0 {
		return ""
	}
	item := s.items[len(s.items)-1]
	s.items = s.items[:len(s.items)-1]
	return item
}

func (s *Stack) peek() string {
	if len(s.items) == 0 {
		return ""
	}
	return s.items[len(s.items)-1]
}

func (s *Stack) isEmpty() bool {
	return len(s.items) == 0
}

func main() {
	stack := Stack{}
	stack.push("Facebook")
	stack.push("Instagram")
	stack.push("Twitch")
	fmt.Println(stack)
	stack.pop()
	fmt.Println(stack)
	stack.push("X")
	fmt.Println(stack)
	fmt.Println(stack.peek(), stack.isEmpty())
}
