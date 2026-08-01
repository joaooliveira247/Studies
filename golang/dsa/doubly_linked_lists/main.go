package main

import "fmt"

type DoublyLinkedList struct {
	Head *ListNode
	Tail *ListNode
}

type ListNode struct {
	Data     string
	Previous *ListNode
	Next     *ListNode
}

func (dll *DoublyLinkedList) printList() {
	current := dll.Head

	for current != nil {
		fmt.Print(current.Data, " -> ")
		current = current.Next
	}
	fmt.Printf("null\n")
}

func (dll *DoublyLinkedList) printListBackward() {
	current := dll.Tail

	fmt.Printf("null")
	for current != nil {
		fmt.Print(" <- ", current.Data)
		current = current.Previous
	}
}

func main() {
	l3 := &ListNode{Data: "X", Next: nil, Previous: nil}
	l2 := &ListNode{Data: "Facebook", Next: l3, Previous: nil}
	l1 := &ListNode{Data: "Instagram", Next: l2, Previous: nil}
	l3.Previous = l2
	l2.Previous = l1

	ll := DoublyLinkedList{Head: l1, Tail: l3}
	ll.printList()
	ll.printListBackward()
}
