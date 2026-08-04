package main

import "fmt"

type DoublyLinkedList struct {
	Head   *ListNode
	Tail   *ListNode
	Lenght uint
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

func (dll *DoublyLinkedList) insertNodeAtBeginning(data string) {
	newNode := &ListNode{Data: data}

	if dll.Lenght == 0 {
		dll.Tail = newNode
	} else {
		dll.Head.Previous = newNode
	}

	newNode.Next = dll.Head
	dll.Head = newNode
	dll.Lenght++
}

func (dll *DoublyLinkedList) insertNodeAtEnd(data string) {
	newNode := &ListNode{Data: data, Next: nil, Previous: nil}

	if dll.Lenght == 0 {
		dll.Head = newNode
	} else {
		dll.Tail.Next = newNode
		newNode.Previous = dll.Tail
	}

	dll.Tail = newNode
	dll.Lenght++
}

func (dll *DoublyLinkedList) removeNodeAtBeginning() {
	if dll.Lenght == 0 {
		return
	}

	temp := dll.Head

	if dll.Head == dll.Tail {
		dll.Head = nil
	} else {
		dll.Head.Next.Previous = nil
	}

	dll.Head = dll.Head.Next
	temp.Next = nil
	dll.Lenght--
}

func main() {
	// l3 := &ListNode{Data: "X", Next: nil, Previous: nil}
	// l2 := &ListNode{Data: "Facebook", Next: l3, Previous: nil}
	// l1 := &ListNode{Data: "Instagram", Next: l2, Previous: nil}
	// l3.Previous = l2
	// l2.Previous = l1

	// ll := DoublyLinkedList{Head: l1, Tail: l3}
	ll := DoublyLinkedList{}
	ll.insertNodeAtBeginning("X")
	ll.insertNodeAtBeginning("Facebook")
	ll.insertNodeAtBeginning("Instagram")
	ll.insertNodeAtBeginning("Telegram")
	ll.insertNodeAtEnd("Twitch")
	ll.removeNodeAtBeginning()
	ll.printList()
	ll.printListBackward()
}
