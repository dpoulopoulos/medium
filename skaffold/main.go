package main

import (
	"fmt"
	"time"
)

func main() {
	for {
		fmt.Println("Hello world! Skaffold is live!")

		time.Sleep(time.Second * 1)
	}
}