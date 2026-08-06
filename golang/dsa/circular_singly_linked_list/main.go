package main

import (
	"fmt"
	"strings"
)

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
	// for last node or cll with one value
	agg = append(agg, first.Data)

	return strings.Join(agg, " --> ")
}

func main() {
	cl := &CircularLinkedList{}
	fmt.Println(cl)
}
