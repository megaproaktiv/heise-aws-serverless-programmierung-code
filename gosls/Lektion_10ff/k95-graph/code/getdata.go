package k95graph

import (
	"context"
	"fmt"
	"sort"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/expression"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
)

//go:generate moq -out getdata_moq_test.go . WeightsInterface

type WeightsInterface interface {
	Scan(ctx context.Context,
		params *dynamodb.ScanInput,
		optFns ...func(*dynamodb.Options)) (*dynamodb.ScanOutput, error)
}

// Item holds info about the items returned by Scan
type Weight struct {
	Uid       string
	Date      string
	Hectogram float64
}

func GetWeights(client WeightsInterface, uid string, table string) ([]Weight, error) {

	// Filter User
	filt1 := expression.Name("uid").Equal(expression.Value(uid))

	proj := expression.NamesList(expression.Name("uid"),
		expression.Name("date"),
		expression.Name("hectogram"),
	)
	expr, err := expression.NewBuilder().WithFilter(filt1).WithProjection(proj).Build()
	if err != nil {
		fmt.Println("Fehler bei building expression:")
		fmt.Println(err.Error())
		return nil, err
	}

	input := &dynamodb.ScanInput{
		ExpressionAttributeNames:  expr.Names(),
		ExpressionAttributeValues: expr.Values(),
		FilterExpression:          expr.Filter(),
		ProjectionExpression:      expr.Projection(),
		TableName:                 aws.String(table),
	}

	resp, err := client.Scan(context.TODO(), input)
	if err != nil {
		fmt.Println("Fehler beim Scannen der Tabelle:")
		fmt.Println(err.Error())
		return nil, err
	}

	weightArray := []Weight{}
	if len(resp.Items) > 0 {
		err = attributevalue.UnmarshalListOfMaps(resp.Items, &weightArray)
	}

	sort.Slice(weightArray, func(i, j int) bool {
		return weightArray[i].Date < weightArray[j].Date
	})
	return weightArray, nil

}
