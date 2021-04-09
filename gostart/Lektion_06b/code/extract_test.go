package extract_test

import(
   "fmt"
   "encoding/json"
   "io/ioutil"
   "os"
  "testing"
  "github.com/aws/aws-lambda-go/events"
  "extract"
  "github.com/stretchr/testify/assert"
)

func TestGet(t *testing.T){
	var event events.S3Event;

	const testfile = "put.json"

	jsonFile, err := os.Open(testfile)
	if err != nil {
		fmt.Println(err)
		panic(err)
	}
	fmt.Println("Successfully Opened ", testfile)
	defer jsonFile.Close()

	byteValue, _ := ioutil.ReadAll(jsonFile)
	if err != nil {
		print(err)
	}

	err = json.Unmarshal([]byte(byteValue), &event)

	expectedKey := "Funny.jpg"
	realKey := extract.Get(event);

	assert.Equal(t, expectedKey,realKey)
}
