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

func (cl *CircularLinkedList) insertNodeAtBeginnig(data string) {
	newNode := &ListNode{Data: data}

	if cl.Length == 0 || cl.Last == nil {
		cl.Last = newNode
	} else {
		newNode.Next = cl.Last.Next
	}

	cl.Last.Next = newNode
	cl.Length++
}

func (cl *CircularLinkedList) insertNodeAtEnd(data string) {
	newNode := &ListNode{Data: data}

	if cl.Last == nil || cl.Length == 0 {
		cl.Last = newNode
		cl.Last.Next = cl.Last
	} else {
		newNode.Next, cl.Last.Next = cl.Last.Next, newNode
		cl.Last = newNode
	}
	cl.Length++
}

func main() {
	cl := &CircularLinkedList{}
	cl.insertNodeAtBeginnig("X")
	cl.insertNodeAtBeginnig("Instagram")
	cl.insertNodeAtBeginnig("Facebook")
	fmt.Println(cl)
}
