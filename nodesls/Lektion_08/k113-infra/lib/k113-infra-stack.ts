import { Construct, Stack, StackProps, CfnOutput }  from '@aws-cdk/core';
import { NodejsFunction }  from '@aws-cdk/aws-lambda-nodejs';
import { Runtime }  from '@aws-cdk/aws-lambda';
import {RetentionDays} from '@aws-cdk/aws-logs';
import * as path from 'path';


export class K113InfraStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const bmiFn = new NodejsFunction(this, 'fn', {
        functionName: "bmi",
        entry: path.join(__dirname, '../code/index.js'),
        runtime: Runtime.NODEJS_14_X,
        memorySize: 1024,
        logRetention: RetentionDays.THREE_MONTHS,
        reservedConcurrentExecutions: 1
      }
    );


  }
}
