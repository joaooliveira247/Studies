package json

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
)

type Dog struct {
	Name  string `json:"name"`
	Age   uint   `json:"age"`
	Breed string `json:"breed"`
}


func ToJSON() {
	d1 := Dog{"Thor", 5, "mixed-breed"}
	fmt.Println(d1)

	dog1JSON, err := json.Marshal(d1)

	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(bytes.NewBuffer(dog1JSON))

	d2 := map[string]string{
		"name": "Tobby",
		"age": "7",
		"breed": "Poodle",
	}

	dog2JSON, err :=json.Marshal(d2)

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(bytes.NewBuffer(dog2JSON))

}