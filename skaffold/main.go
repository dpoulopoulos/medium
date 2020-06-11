package main

import (
	"fmt"
	"time"
)

func main() {
	for {
		fmt.Println("Hello world! Hello from Skaffold!")

		time.Sleep(time.Second * 1)
	}
}