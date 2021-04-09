import * as cdk from '@aws-cdk/core';
import * as s3 from '@aws-cdk/aws-s3';
import * as s3Deployment from '@aws-cdk/aws-s3-deployment';

export class K113WebsiteStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const myBucket = new s3.Bucket(this, 'k113.megaproaktiv.de', {
      bucketName: "k113.megaproaktiv.de",
      publicReadAccess: true,
      removalPolicy: cdk.RemovalPolicy.RETAIN,
      websiteIndexDocument: 'index.html',
    });
    const deployment = new s3Deployment.BucketDeployment(
      this,
      'deployStaticWebsite',
      {
        sources: [s3Deployment.Source.asset('./website')],
        destinationBucket: myBucket,
      }
    );
  }
}
