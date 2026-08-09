package main

import (
	"fmt"
	"strings"
)

type ListNode[U any] struct {
	Data U
	Next *ListNode[U]
}

type Queue[T any] struct {
	front  *ListNode[T]
	rear   *ListNode[T]
	length uint
}

func (q Queue[T]) String() string {
	if q.length == 0 || q.front == nil {
		return "[ FRONT | REAR ] (empty queue)"
	}

	var items []string
	current := q.front
	for current != nil {
		items = append(items, fmt.Sprintf(" %v ", current.Data))
		current = current.Next
	}

	queueLine := fmt.Sprintf("[ %s ]", strings.Join(items, " -> "))

	frontLabel := "FRONT"
	rearLabel := "REAR"

	padding := len(queueLine) - len(frontLabel) - len(rearLabel)
	if padding < 1 {
		padding = 1
	}

	labels := frontLabel + strings.Repeat(" ", padding) + rearLabel

	var sb strings.Builder
	sb.WriteString(labels + "\n")
	sb.WriteString(queueLine)

	return sb.String()
}

func (q *Queue[T]) Length() uint {
	return q.length
}

func (q *Queue[T]) isEmpty() bool {
	return q.length == 0
}

func (q *Queue[T]) Enqueue(data T) {
	temp := &ListNode[T]{Data: data}

	if q.isEmpty() {
		q.front = temp
	} else {
		q.rear.Next = temp
	}

	q.rear = temp
	q.length++
}

func (q *Queue[T]) Dequeue() T {
	if q.Length() == 0 || q.front == nil {
		var zero T
		return zero
	}

	result := q.front.Data
	q.front = q.front.Next
	q.length--

	return result
}

func main() {
	q := Queue[string]{}
	q.Enqueue("Facebook")
	q.Enqueue("X")
	q.Enqueue("Instagram")
	fmt.Println(q)
	q.Dequeue()
	fmt.Println(q)
}
