package main

import (
	"fmt"
	"strings"
)

type StackLinkedList struct {
	Top    *StackNode
	Lenght uint
}

type StackNode struct {
	Data string
	Next *StackNode
}

func (sl StackLinkedList) String() string {
	if sl.Top == nil || sl.Lenght == 0 {
		return "[ ] (empty stack)"
	}

	var items []string
	maxLen := 0

	current := sl.Top
	for current != nil {
		items = append(items, current.Data)
		if len(current.Data) > maxLen {
			maxLen = len(current.Data)
		}
		current = current.Next
	}

	var sb strings.Builder

	sb.WriteString("┌" + strings.Repeat(" ", maxLen+2) + "┐\n")

	for _, item := range items {
		itemFormatted := fmt.Sprintf("│ %-*s │\n", maxLen, item)
		sb.WriteString(itemFormatted)
	}

	sb.WriteString("└" + strings.Repeat("─", maxLen+2) + "┘")

	return sb.String()
}

func (sl *StackLinkedList) push(data string) {
	newNode := &StackNode{Data: data}

	newNode.Next = sl.Top
	sl.Top = newNode
	sl.Lenght++
	fmt.Printf("Adding %s to stack...\n", data)
}

func (sl *StackLinkedList) pop() string {
	result := sl.Top.Data
	sl.Top = sl.Top.Next
	sl.Lenght--

	fmt.Printf("Removing %s from stack...\n", result)
	return result
}

func main() {
	stack := StackLinkedList{}
	stack.push("Instagram")
	stack.push("Facebook")
	stack.push("Twitch")
	fmt.Println(stack)
	stack.pop()
	fmt.Println(stack)
}
