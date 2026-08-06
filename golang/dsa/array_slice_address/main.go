package main

import (
	"fmt"
	"reflect"
	"unsafe"
)

func main() {
	arr := [5]int{10, 20, 30, 40, 50}

	fmt.Println("Array addresses (8 bytes steps)")
	for idx, value := range arr {
		fmt.Printf(
			"Element: [%d]: Value = %d | Address = %p\n",
			idx,
			value,
			&arr[idx],
		)
	}

	// slice struct implementation

	slc := arr[1:4]

	sliceHeader := (*reflect.SliceHeader)(unsafe.Pointer(&slc))

	fmt.Println("\nSlice intern struct representation")
	fmt.Printf("Adress of arr[0]: %p\n", &arr[0])
	fmt.Printf("Adress of arr[1]: %p\n", &arr[1])
	fmt.Printf("Pointer of slc field('Data'): 0x%x\n", sliceHeader.Data)
	fmt.Printf("Slice length field('Len'): %d\n", sliceHeader.Len)
	fmt.Printf("Slice Capacity field('Cap'): %d\n", sliceHeader.Cap)

}
