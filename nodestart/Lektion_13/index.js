const {S3Client, ListBucketsCommand} = require("@aws-sdk/client-s3")

const list = async () => {
  const client = new S3Client();
  // Leere Parameter
  const command = new ListBucketsCommand({});
  try {
    const data = await client.send(command);
    console.log(data)
  } catch(error){
    console.log(error)
  }
}

list();
