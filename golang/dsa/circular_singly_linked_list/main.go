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

func (cl *CircularLinkedList) String() string {
	if cl.Length == 0 {
		return ""
	}

	var agg []string

	first := cl.Last.Next
	for first != cl.Last {
		agg = append(agg, first.Data)
		first = first.Next
	}
	return strings.Join(agg, " --> ")
}

func main() {
	cl := &CircularLinkedList{}
}
