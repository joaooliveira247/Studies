package main

import (
	"fmt"
	"strings"
)

type LinkedList struct {
	Head *Node
}

type Node struct {
	value string
	next  *Node
}

func (ll *LinkedList) insertAtBeginning(data string) {
	newNode := &Node{value: data, next: ll.Head}
	ll.Head = newNode
}

func (ll *LinkedList) insertAtEnd(data string) {
	newNode := &Node{value: data, next: nil}

	if ll.Head == nil {
		ll.Head = newNode
		return
	}

	current := ll.Head

	for current.next != nil {
		current = current.next
	}

	current.next = newNode
}

func (ll *LinkedList) removeAtBeginning() {
	if ll.Head == nil {
		return
	}
	ll.Head = ll.Head.next
}

func (ll *LinkedList) removeAtEnd() {
	if ll.Head == nil || ll.Head.next == nil {
		return
	}

	previous := ll.Head

	for previous.next.next != nil {
		previous = previous.next
	}

	previous.next = nil
}

func (ll LinkedList) String() string {
	values := []string{}

	current := ll.Head
	for current != nil {
		values = append(values, current.value)
		current = current.next
	}

	return fmt.Sprintf("[ %s ]", strings.Join(values, ", "))
}

func main() {
	nodes := &LinkedList{}
	nodes.insertAtBeginning("Youtube")
	nodes.insertAtBeginning("Instagram")
	fmt.Println(nodes)
	nodes.insertAtEnd("Telegram")
	nodes.insertAtEnd("X")
	nodes.insertAtEnd("Kick")
	nodes.insertAtEnd("Twitch")
	fmt.Println(nodes)
	nodes.removeAtBeginning() // remove instagram
	fmt.Println(nodes)
	nodes.removeAtEnd() // remove twitch
	fmt.Println(nodes)
}
