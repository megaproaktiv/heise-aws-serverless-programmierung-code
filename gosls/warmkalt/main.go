// main.go
package main

import (
	"fmt"
	"github.com/aws/aws-lambda-go/lambda"
	"os"
)

func hello() (string, error) {

	_, err := os.Stat("/tmp/test.txt")
	if os.IsNotExist(err) {
		fmt.Println(err)
		fmt.Println("Datei existiert nicht, erstelle Datei")
		f, _ := os.Create("/tmp/test.txt")
		defer f.Close()
		_, err := f.WriteString("Hello World")
		if err != nil {
			fmt.Println(err)
		}
	} else {
		fmt.Println("Datei existiert bereits.")
	}

	return "Hello ƛ !", nil
}

func main() {
	// Make the handler available for Remote Procedure Call by AWS Lambda
	lambda.Start(hello)
}
