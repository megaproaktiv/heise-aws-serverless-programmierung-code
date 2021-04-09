import * as cdk from '@aws-cdk/core';
import {Runtime} from '@aws-cdk/aws-lambda';
import {NodejsFunction} from '@aws-cdk/aws-lambda-nodejs';
import {RetentionDays} from '@aws-cdk/aws-logs';
import * as path from 'path';
import {LambdaRestApi} from '@aws-cdk/aws-apigateway';
import {CfnOutput} from '@aws-cdk/core';

export class K113Stack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const bmiFn = new NodejsFunction( this, 'fn' , {
      entry:  path.join(__dirname, '../code/index.js'),
      runtime:  Runtime.NODEJS_14_X,
      memorySize: 1024,
      logRetention: RetentionDays.THREE_MONTHS,
      reservedConcurrentExecutions: 1
    })

    const api = new LambdaRestApi( this, 'lapi', {
      handler: bmiFn,
      proxy: false
    }
    );
    const bmi = api.root.addResource('bmi');
    bmi.addMethod('GET');

    new CfnOutput(this, "url",
      {
        value: api.url
      })



  }
}
