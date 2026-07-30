package main

import (
	"fmt"
	"strings"
)

type Node struct {
	value string
	next  *Node
}

type LinkedList struct {
	Head *Node
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

func (ll *LinkedList) reverseList() {
	current := ll.Head
	var previous *Node
	var next *Node

	for current != nil {
		next = current.next
		current.next = previous
		previous = current
		current = next
	}

	ll.Head = previous
}

func main() {
	nodes := &LinkedList{
		Head: &Node{
			value: "X",
			next: &Node{
				value: "Youtube",
				next: &Node{
					value: "Instagram",
					next: nil,
				},
			},
		},
	}

	fmt.Println(nodes)
	nodes.reverseList()
	fmt.Println(nodes)
}
