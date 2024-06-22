package main

import (
	"fmt"
	"math"
)

type Form interface {
	area() float64
}

type Rectangle struct {
	width  float64
	height float64
}

type Circle struct {
	radius float64
}

func writeArea(f Form) {
	fmt.Printf("Area: %.2f ", f.area())
}

func (r Rectangle) area() float64 {
	return r.height * r.width
}

func (r Circle) area() float64 {
	return math.Pi * (r.radius * r.radius)
}

func main() {
	r1 := Rectangle{10, 4}
	writeArea(r1)
	c1 := Circle{10}
	writeArea(c1)
}
