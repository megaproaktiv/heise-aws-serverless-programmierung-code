package main

import (
	"context"
	"os"
	"encoding/base64"
	"fmt"
	//"net/http"
	"k95graph"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
)

const imageFile = "/tmp/output.png"

func toBase64(b []byte) string {
	return base64.StdEncoding.EncodeToString(b)
}

func handler(ctx context.Context, request events.APIGatewayProxyRequest)(events.APIGatewayProxyResponse, error) {


	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		panic("unable to load SDK config, " + err.Error())
	}
	client := dynamodb.NewFromConfig(cfg)
	
	items,_ := k95graph.GetWeights(client, "1", "daily-weight")

	k95graph.Render(items,imageFile)


	fileInfos, err := os.Stat(imageFile)
	fmt.Println("Dateigroesse:", fileInfos.Size())

	data, err := os.ReadFile(imageFile)
	if err != nil {
		fmt.Println("Fehler beim Image lesen:")
		fmt.Println(err.Error())	
	}else{
		fmt.Println("Lesen Bild erfolgreich")
	}
	

	var base64Encoding string
	// mimeType := http.DetectContentType(data)
	// switch mimeType {
	// 	case "image/jpeg":
	// 		base64Encoding += "data:image/jpeg;base64,"
	// 	case "image/png":
	// 		base64Encoding += "data:image/png;base64,"
	// }
	base64Encoding += toBase64(data)

	return events.APIGatewayProxyResponse{
		Body:       base64Encoding,
		Headers: map[string]string{
			"Content-Type": "image/png"},
		IsBase64Encoded: true,
		StatusCode: 200,
	}, nil
}

func main() {
	lambda.Start(handler)
}

