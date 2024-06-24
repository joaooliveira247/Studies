package address

import "testing"

func TestAddress(t *testing.T) {
	testAddress := "Avenida Brasil 1507"
	result := AddressType(testAddress)

	if result != "Avenida" {
		t.Error("Wrong type return.")
	}
}