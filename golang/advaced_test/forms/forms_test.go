package forms

import (
	"math"
	"testing"
)

func TestArea(t *testing.T) {
	t.Run("Rectangle", func(t *testing.T) {
		ret := Rectangle{10, 12}
		retIn := ret.Area()
		retOut := float64(120)

		if retOut != retIn {
			t.Fatalf("wait %f got %f", retOut, retIn)
		}
	})

	t.Run("Circle", func(t *testing.T) {
		circ := Circle{10}
		retIn := circ.Area()
		retOut := float64(math.Pi * 100)

		if retOut != retIn {
			t.Fatalf("wait %f got %f", retOut, retIn)
		}

	})
}
