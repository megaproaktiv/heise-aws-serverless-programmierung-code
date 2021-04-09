//
// Promise Beispiel
//
const AWS = require('aws-sdk')
var req = new AWS.EC2({region: 'eu-central-1'}).describeInstances();
const promise= req.promise();
// Mach was anderes hier
promise.then( (data) => {
  console.log(JSON.stringify(data))
});