package main

import (
	"fmt"
)

// Graph (struct) - represents an adjacency list graph
type Graph struct {
	vertices []*Vertex
}

// Vertex (struct)
type Vertex struct {
	key       int
	adjacents []*Vertex
}

func (g *Graph) Print() {
	for _, v := range g.vertices {
		fmt.Printf("\nVertex %d : ", v.key)
		for _, v := range v.adjacents {
			fmt.Printf(" %d ", v.key)
		}
	}
	fmt.Println()
}

// Add Vertex
func (g *Graph) AddVertex(k int) error {
	if contains(g.vertices, k) {
		return fmt.Errorf(
			"Vertex %v not added 'cause it is an existing key",
			k,
		)
	}

	g.vertices = append(g.vertices, &Vertex{key: k})
	return nil
}

// Add Edge - adds an edge to the graph
func (g *Graph) AddEdge(from, to int) error {
	// get vertex
	fromVertex := g.getVertex(from)
	toVertex := g.getVertex(to)
	// check error
	if fromVertex == nil || toVertex == nil {
		return fmt.Errorf("One of Vertex doesn't exists")
	} else if contains(fromVertex.adjacents, toVertex.key) {
		return fmt.Errorf(
			"%d already existis in %d Vertex",
			toVertex.key,
			fromVertex.key,
		)
	}
	// add edge
	fromVertex.adjacents = append(fromVertex.adjacents, toVertex)
	// 10:38
	return nil
}

// getVertex
func (g *Graph) getVertex(k int) *Vertex {
	for i, v := range g.vertices {
		if v.key == k {
			return g.vertices[i]
		}
	}
	return nil
}

// contains
func contains(vertices []*Vertex, key int) bool {
	if len(vertices) == 0 {
		return false
	} else if vertices[0].key == key {
		return true
	} else {
		return contains(vertices[1:], key)
	}
}

func main() {
	graphTest := Graph{}
	for v := range 5 {
		graphTest.AddVertex(v)
	}
	fmt.Println(contains(graphTest.vertices, 5))
	graphTest.AddEdge(2, 4)
	graphTest.AddEdge(4, 2)
	graphTest.AddEdge(4, 2)
	graphTest.Print()
}
