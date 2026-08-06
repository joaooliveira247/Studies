package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	fastPointer := head
	slowPointer := head

	for fastPointer != nil && fastPointer.Next != nil {
		fastPointer = fastPointer.Next.Next
		slowPointer = slowPointer.Next

		if fastPointer == slowPointer {
			return true
		}
	}
	return false
}

func main() {
	l1 := &ListNode{Val: 1}
	l2 := &ListNode{Val: 2}

	l1.Next, l2.Next = l2, l1

	fmt.Println(hasCycle(l1))
}
