package k95graph_test

import (
	"context"
	
	"os"
	"fmt"
	"k95graph"
	"testing"

	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/stretchr/testify/assert"
)

func TestRender(t *testing.T) {

	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		panic("unable to load SDK config, " + err.Error())
	}
	client := dynamodb.NewFromConfig(cfg)
	
	fileName := "output.png"
	err = os.Remove(fileName)

	if err != nil {
	  fmt.Println(err)
	
	}

	items,_ := k95graph.GetWeights(client, "1", "daily-weight")
	k95graph.Render(items,fileName)

	_, err = os.Stat(fileName)
	assert.Equal(t, false,os.IsNotExist(err), "Bild sollte erzeugt werden")

}
