package address

import "testing"

type TestCase struct {
	input  string
	output string
}

func TestAddress(t *testing.T) {
	t.Parallel()
	testAddress := "Avenida Brasil 1507"
	result := AddressType(testAddress)

	if result != "Avenida" {
		t.Error("Wrong type return.")
	}
}

func TestAddressWithStruct(t *testing.T) {
	t.Parallel()
	testCases := []TestCase{
		{
			"Rua das flores", "Rua",
		},
		{
			"Avenida Brasil 1507", "Avenida",
		},
		{
			"Estrada da posse", "Estrada",
		},
		{
			"Rodovia amaral peixoto", "Rodovia",
		},
		{
			"Travessa cardoso", "Pattern not found",
		},
	}

	for _, case_ := range testCases {
		addressType := AddressType(case_.input)
		if addressType != case_.output {
			t.Errorf("Input type %s wait: %s got: %s", case_.input, case_.output, addressType)
		}
	}
}
