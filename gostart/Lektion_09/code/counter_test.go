package counter_test

import (
	"counter"
	"testing"
	"github.com/stretchr/testify/assert"
)

func TestCountStacks(t *testing.T) {
	expectedValues := 2;

	// bytes := []byte(str_emp)
	// var res Response
	// json.Unmarshal(bytes, &res)

	
	computedValue := counter.Count()

	assert.Equal(t,expectedValues, computedValue)

}