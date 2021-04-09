package main

import (
  "context"
  "fmt"
  "github.com/aws/aws-lambda-go/lambda"
  "github.com/aws/aws-lambda-go/events"
)

func handler(ctx context.Context, s3Event events.S3Event) {
	// See https://github.com/aws/aws-lambda-go/tree/master/events
	// Handle only one event
        fmt.Println(s3Event.Records[0].S3.Object.Key);
}

func main() {

	lambda.Start(handler)

}
