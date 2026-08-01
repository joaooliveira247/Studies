package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1, l2 *ListNode) *ListNode {
	mergedList := &ListNode{}
	tail := mergedList

	for l1 != nil && l2 != nil {
		if l1.Val <= l2.Val {
			tail.Next = &ListNode{Val: l1.Val}
			l1 = l1.Next
		} else {
			tail.Next = &ListNode{Val: l2.Val}
			l2 = l2.Next
		}
		tail = tail.Next
	}

	if l1 == nil {
		tail.Next = l2
	} else {
		tail.Next = l1
	}

	return mergedList.Next
}

func main() {
	ll := mergeTwoLists(
		&ListNode{
			Val:  2,
			Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: nil}},
		},
		&ListNode{
			Val:  4,
			Next: &ListNode{Val: 5, Next: &ListNode{Val: 6, Next: nil}},
		},
	)

	current := ll
	for current != nil {
		fmt.Print(current.Val, " -> ")
		current = current.Next
	}
	fmt.Printf("null\n")
}
