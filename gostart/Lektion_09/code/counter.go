package counter

import (
	"context"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/cloudformation"
)


// Count counts the number of Stacks in the current account
func Count() (int){
	cfg, err := config.LoadDefaultConfig(context.TODO())
    if err != nil {
        panic("unable to load SDK config, " + err.Error())
	}
	
	client := cloudformation.NewFromConfig(cfg);
	input := &cloudformation.DescribeStacksInput{}

	resp, _ := client.DescribeStacks(context.TODO(), input)
	count := len(resp.Stacks)
	return count
}


