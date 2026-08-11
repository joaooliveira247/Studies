package main

import "fmt"

// Heap are like binary tree or priority queues, it's like a 'binarry tree array'.
// This file has the max heap implementation

// MaxHeap (Struct)
type MaxHeap struct {
	array []int
}

// Insert (Method) - adds an element to the heap
func (h *MaxHeap) Insert(key int) {
	h.array = append(h.array, key)
	h.maxHeapifyUp(len(h.array) - 1)
}

// Extract (Method) - returns the largest key, and removes it from the heap
func (h *MaxHeap) Extract() int {
	if len(h.array) == 0 {
		fmt.Println("Cannot extract because array length is 0")
		return -1
	}

	extracted := h.array[0]

	l := len(h.array) - 1
	h.array[0] = h.array[l]
	h.array = h.array[:l]

	h.maxHeapifyDown(0)

	return extracted
}

// maxHeapifyUp (Method) will heapify from bottom top
func (h *MaxHeap) maxHeapifyUp(idx int) {
	for h.array[parent(idx)] < h.array[idx] {
		h.swap(parent(idx), idx)
		idx = parent(idx)
	}
}

// maxHeapifyDown (Method) - will heapify from top to bottom
func (h *MaxHeap) maxHeapifyDown(idx int) {
	lastIndex := len(h.array) - 1
	l, r := left(idx), right(idx)

	childToCompare := 0

	for l <= lastIndex {
		if l == lastIndex {
			childToCompare = l
		} else if h.array[l] > h.array[r] {
			childToCompare = l
		} else {
			childToCompare = r
		}

		if h.array[idx] < h.array[childToCompare] {
			h.swap(idx, childToCompare)
			idx = childToCompare
			l, r = left(idx), right(idx)
		} else {
			return
		}
	}
}

// swap (Method) - swap keys in the array
func (h *MaxHeap) swap(i1, i2 int) {
	h.array[i1], h.array[i2] = h.array[i2], h.array[i1]
}

// parent (function) - get the parent index
func parent(i int) int {
	return (i - 1) / 2
}

// left (function)
func left(i int) int {
	return 2*i + 1
}

// right (function)
func right(i int) int {
	return 2*i + 2
}

func main() {
	m := MaxHeap{}
	fmt.Println(m)
	for _, v := range []int{10, 20, 30, 5, 7, 9, 11, 13, 15, 17} {
		m.Insert(v)
	}
	fmt.Println(m)

	for range 5 {
		m.Extract()
		fmt.Println(m)
	}

}
