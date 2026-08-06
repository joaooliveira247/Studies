package main

import "strings"

type CircularLinkedList struct {
	Length int
	Last   *ListNode
}

type ListNode struct {
	Data string
	Next *ListNode
}

func main() {
	cl := &CircularLinkedList{}
}
