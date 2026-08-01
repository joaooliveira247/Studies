package main

import "fmt"

const ArraySize = 7

// Hash Table part (Array)
// HashTable (struct)
// Insert (method)
// Search (method)
// Delete (method)
type HashTable struct {
	array [ArraySize]*bucket
}

func (h *HashTable) Insert(key string) {
	index := hash(key)
	h.array[index].insert(key)
}

func (h *HashTable) Search(key string) bool {
	index := hash(key)
	return h.array[index].search(key)
}

func (h *HashTable) Delete(key string) {
	index := hash(key)
	h.array[index].delete(key)
}

// Bucket part (Linked list)
// bucket (struct)
// bucketNode (struct)
// insert (method)
// Search (method)
// Delete (method)
type bucket struct {
	Head *bucketNode
}

type bucketNode struct {
	key  string
	next *bucketNode
}

func (b *bucket) insert(k string) {
	newNode := &bucketNode{key: k}
	newNode.next = b.Head
	b.Head = newNode
}

func (b *bucket) search(k string) bool {
	currentNode := b.Head

	for currentNode != nil {
		if currentNode.key == k {
			return true
		}
		currentNode = currentNode.next
	}
	return false
}

func (b *bucket) delete(k string) {

	if b.Head.key == k {
		b.Head = b.Head.next
		return
	}

	previoursNode := b.Head

	for previoursNode.next != nil {
		if previoursNode.next.key == k {
			previoursNode.next = previoursNode.next.next
			return
		}
		previoursNode = previoursNode.next
	}
}

// hash (function)
func hash(key string) int {
	sum := 0

	for _, value := range key {
		sum += int(value)
	}

	return sum % ArraySize
}

// Init (function) start HashTable struct with bucket struct intead nil
func Init() *HashTable {
	result := &HashTable{}

	for i := range result.array {
		result.array[i] = &bucket{}
	}
	return result
}

func main() {
	/*
		testHashTable := Init()
		fmt.Println(testHashTable)
		fmt.Println(hash("RANDY"))

		testBucket := &bucket{}
		testBucket.insert("RANDY")
		testBucket.insert("JAMIE")
		fmt.Printf("%+v\n", testBucket.Head)
		fmt.Println("RANDY", testBucket.search("RANDY"))
		testBucket.delete("JAMIE")
		fmt.Println("JAMIE", testBucket.search("JAMIE"))
		fmt.Println("ERIC", testBucket.search("ERIC"))
	*/
	hashTable := Init()

	list := []string{
		"JAMIE",
		"AMANDA",
		"CAROL",
		"JOHN",
		"ANNA",
		"PETER",
		"RANDY",
	}

	for _, v := range list {
		hashTable.Insert(v)
	}

	fmt.Println(hashTable.array[1].Head.key)
}
