package k95graph_test

import (
	"context"
	"encoding/json"
	"io/ioutil"
	"fmt"
		"k95graph"
	"testing"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/stretchr/testify/assert"
)

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
		Date: "2020-03-10",
		Hectogram: float64(950),
	}

	assert.Equal(t,expectedFirstItem, result[0])
}