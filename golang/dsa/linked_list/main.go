package main

import "fmt"

type Node struct {
	value int
	next  *Node
}

func (n *Node) printList() {
	current := n
	for current != nil {
		fmt.Print(current.value, " --> ")
		current = current.next
	}
	fmt.Println("null")
}

func (n *Node) length() (size int) {
	current := n
	for current != nil {
		size++
		current = current.next
	}
	return size
}

func main() {
	nodes := Node{
		value: 1,
		next:  &Node{value: 2, next: &Node{value: 3, next: nil}},
	}
	nodes.printList()
	fmt.Println(nodes.length())
}
