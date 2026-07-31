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

func (ll *LinkedList) findWhereLoopStarts() *Node {
	fastPointer := ll.Head
	slowPointer := ll.Head

	for fastPointer != nil && fastPointer.next != nil {
		fastPointer = fastPointer.next.next
		slowPointer = slowPointer.next

		if fastPointer == slowPointer {
			break
		}
	}

	if slowPointer != fastPointer {
		return nil
	}

	temp := ll.Head

	for temp != slowPointer {
		temp = temp.next
		slowPointer = slowPointer.next
	}

	return temp
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
	node4 := &Node{
		value: "Instagram",
	}
	node3 := &Node{
		value: "Facebook",
		next:  node4,
	}
	node2 := &Node{
		value: "X",
		next:  node3,
	}
	node1 := &Node{
		value: "Youtube",
		next:  node2,
	}

	node4.next = node2

	ll := &LinkedList{Head: node1}

	fmt.Println(ll.findWhereLoopStarts())

}
