const {S3Client, ListBucketsCommand} = require("@aws-sdk/client-s3")

exports.handler = async (event) => {
    const client = new S3Client();
    // Leere Parameter
    const command = new ListBucketsCommand({});
    try {
      const data = await client.send(command);
      console.log(data)
      const response = {
        statusCode: 200,
        body: JSON.stringify(data)
      };
      return response;
    } catch(error){
        return {
            statusCode: 500,
            body: JSON.stringify(error)
        };
    }
};
