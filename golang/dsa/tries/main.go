package main

import "fmt"

const AlphabetSize uint8 = 26

// Node (struct) - represents each node in trie
type Node struct {
	children [AlphabetSize]*Node
	isEnd    bool
}

// Trie (struct) - represents a trie and has a pointer to
// A trie can used to autocomplete... it's like a tree with ll
type Trie struct {
	root *Node
}

// InitTrie (func) - create a empty trie
func InitTrie() *Trie {
	trie := &Trie{root: &Node{}}
	return trie
}

// Insert (method) - will take a word and add it to the trie
func (t *Trie) Insert(word string) {

	currentNode := t.root
	for idx, _ := range word {
		charIdx := word[idx] - 'a'
		if currentNode.children[charIdx] == nil {
			currentNode.children[charIdx] = &Node{}
		}
		currentNode = currentNode.children[charIdx]
	}
	currentNode.isEnd = true
}

// Search (method) - will take a word and return true if that word is in trie
func (t *Trie) Search(word string) bool {
	currentNode := t.root
	for idx, _ := range word {
		charIdx := word[idx] - 'a'
		if currentNode.children[charIdx] == nil {
			return false
		}
		currentNode = currentNode.children[charIdx]
	}
	if currentNode.isEnd {
		return true
	}

	return false
}

func main() {
	testTrie := InitTrie()

	for _, v := range []string{"aragorn", "aragon", "argon", "eragon", "oregon"} {
		testTrie.Insert(v)
	}

	fmt.Printf("(oregano): %t\n", testTrie.Search("oregano"))
	fmt.Printf("(argon): %t\n", testTrie.Search("argon"))
}
