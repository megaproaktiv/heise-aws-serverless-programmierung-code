package main

import(
	"counter"
	"context"
	"fmt"
	"github.com/aws/aws-lambda-go/lambda"
)

func handler(ctx context.Context) {
	count := counter.Count()
	fmt.Println("Counting CloudFormation Stacks: ",count)
}


func main() {
	lambda.Start(handler)
}
