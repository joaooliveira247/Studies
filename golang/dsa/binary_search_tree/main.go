package main

import "fmt"

// Node
type Node struct {
	Key   int
	Left  *Node
	Right *Node
}

// Insert method
func (n *Node) Insert(k int) {
	if n.Key == 0 && k != 0 {
		n.Key = k
	}

	if n.Key < k {
		//move right
		if n.Right == nil {
			n.Right = &Node{Key: k}
		} else {
			n.Right.Insert(k)
		}
	} else if n.Key > k {
		//move left
		if n.Left == nil {
			n.Left = &Node{Key: k}
		} else {
			n.Left.Insert(k)
		}
	}

}

// Search method

func (n *Node) Search(k int) bool {

	if n == nil {
		return false
	}

	if n.Key < k {
		// move right
		return n.Right.Search(k)
	} else if n.Key > k {
		//move left
		return n.Left.Search(k)
	}

	return true
}

func main() {
	tree := &Node{}
	tree.Insert(100)
	tree.Insert(50)
	tree.Insert(30)
	fmt.Println(tree, tree.Search(2), tree.Search(30))
}
