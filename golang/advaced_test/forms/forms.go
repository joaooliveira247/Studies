package forms

import (
	"fmt"
	"math"
)

type Form interface {
	area() float64
}

type Rectangle struct {
	Width  float64
	Height float64
}

type Circle struct {
	Radius float64
}

func WriteArea(f Form) {
	fmt.Printf("Area: %.2f ", f.area())
}

func (r Rectangle) Area() float64 {
	return r.Height * r.Width
}

func (r Circle) Area() float64 {
	return math.Pi * (r.Radius * r.Radius)
}
