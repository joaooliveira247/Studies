package main

import "fmt"

type TreeNode struct {
	Data  int
	Left  *TreeNode
	Right *TreeNode
}

func insert(node *TreeNode, data int) *TreeNode {
	if node == nil {
		return &TreeNode{Data: data}
	}

	if data <= node.Data {
		node.Left = insert(node.Left, data)
	} else {
		node.Right = insert(node.Right, data)
	}

	return node
}

func preOrder(node *TreeNode) {
	if node == nil {
		return
	}
	fmt.Printf("%d ", node.Data)
	preOrder(node.Left)
	preOrder(node.Right)
}

func inOrder(node *TreeNode) {
	if node == nil {
		return
	}
	inOrder(node.Left)
	fmt.Printf("%d ", node.Data)
	inOrder(node.Right)
}

func postOrder(node *TreeNode) {
	if node == nil {
		return
	}
	postOrder(node.Left)
	postOrder(node.Right)
	fmt.Printf("%d ", node.Data)
}

func main() {
	root := insert(nil, 10)

	insert(root, 2)
	insert(root, 20)
	insert(root, 0)
	insert(root, 3)
	
	preOrder(root)
}
