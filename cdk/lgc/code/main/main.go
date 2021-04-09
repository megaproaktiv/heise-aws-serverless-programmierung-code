package main

import (
	"context"
	"fmt"
	"github.com/aws/aws-lambda-go/lambda"
)

func handler(ctx context.Context) {
	fmt.Println("Hello")
}

func main() {
	lambda.Start(handler)
}
