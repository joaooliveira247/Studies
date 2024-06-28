package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

func check(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func connectDB(stringConnection string) *sql.DB {
	db, err := sql.Open("mysql", stringConnection)
	check(err)
	check(db.Ping())
	fmt.Printf("Connected in %s", stringConnection)
	return db

}

func main() {
	stringConnection := "user:passwd@tcp(localhost:3306)/mydatabase?charset=utf8&parseTime=True&loc=Local"
	db := connectDB(stringConnection)
	defer db.Close()
}
