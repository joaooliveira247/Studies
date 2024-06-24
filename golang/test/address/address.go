package address

import (
	"strings"
)

// AddressType check if a address is valid and return a string with valid type
func AddressType(address string) string {
	validTypes := []string{"rua", "avenida", "estrada", "rodovia"}

	firstWord := strings.Split(address, " ")[0]

	for _, value := range validTypes {
		if value == strings.ToLower(firstWord) {
			return strings.Title(value)
		}
	}
	return "Pattern not found"
}
