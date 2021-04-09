package k95graph_test

import (
	"context"
	"k95graph"
	"testing"
	"errors"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
	"github.com/stretchr/testify/assert"
)

func TestSomethingThatUsesWeightsInterface(t *testing.T) {

	// make and configure a mocked WeightsInterface
	mockedWeightsInterface := &k95graph.WeightsInterfaceMock{
		ScanFunc: func(ctx context.Context, params *dynamodb.ScanInput, optFns ...func(*dynamodb.Options)) (*dynamodb.ScanOutput, error) {
				item1 := k95graph.Weight{
					Date: "2020-03-10",
					Hectogram: float64(950),
					Uid: "1",
				}
				av1, err := attributevalue.MarshalMap(item1)
				if err != nil {
					return nil, errors.New("Could not items")
				}

				item2 := k95graph.Weight{
					Date: "2020-03-01",
					Hectogram: float64(960),
					Uid: "1",
				}

				av2, err := attributevalue.MarshalMap(item2)
				if err != nil {
					return nil, errors.New("Could not items")
				}

				avs := []map[string]types.AttributeValue{
					av1,
					av2,
				}
			
				output := &dynamodb.ScanOutput{
					Items: avs,
				}
				return output, nil

				
		},
	}

	// use mockedWeightsInterface in code that requires WeightsInterface
	// and then make assertions.
	result,_ := k95graph.GetWeights(mockedWeightsInterface,"1","table")

	expectedFirstItem := k95graph.Weight{
		Uid: "1",
		Date: "2020-03-01",
		Hectogram: float64(960),
	}

	assert.Equal(t,expectedFirstItem, result[0])
}
func TestRealThatUsesWeightsInterface(t *testing.T) {

	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		panic("unable to load SDK config, " + err.Error())
	}

	client := dynamodb.NewFromConfig(cfg)
	

	// use mockedWeightsInterface in code that requires WeightsInterface
	// and then make assertions.
	result,_ := k95graph.GetWeights(client,"1","daily-weight")

	expectedFirstItem := k95graph.Weight{
		Uid: "1",
		Date: "2020-02-01",
		Hectogram: float64(990),
	}

	assert.Equal(t,expectedFirstItem, result[0])
}