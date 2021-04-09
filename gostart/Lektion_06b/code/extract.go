package extract

import (
	"github.com/aws/aws-lambda-go/events"
)

func Get(s3event events.S3Event) string {
  return s3event.Records[0].S3.Object.Key
}
