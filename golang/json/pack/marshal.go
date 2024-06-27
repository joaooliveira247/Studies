package json

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"os"
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
		"name":  "Tobby",
		"age":   "7",
		"breed": "Poodle",
	}

	dog2JSON, err := json.Marshal(d2)

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(bytes.NewBuffer(dog2JSON))

}

type UserInfo struct {
	UserId    int    `json:"userId"`
	Id        int    `json:"id"`
	Title     string `json:"title"`
	Completed bool   `json:"completed"`
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func FromJSON() {
	var userInfo UserInfo
	data, err := os.ReadFile("./example.json")
	check(err)
	err = json.Unmarshal(data, &userInfo)
	check(err)
	fmt.Println(userInfo)
}
