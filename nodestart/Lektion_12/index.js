// Aufruf S3 mit node SDK
aws = require("aws-sdk")
  
var s3 = new aws.S3();
 
s3.listBuckets( function(err,data){
  if (err) {
    console.log(err, err.stack);
  }else{
    console.log(data);
  }
  }
)
