import { Construct, Stack, StackProps }  from '@aws-cdk/core';
import { NodejsFunction }  from '@aws-cdk/aws-lambda-nodejs';
import { Runtime }  from '@aws-cdk/aws-lambda';
import * as path from 'path';

export class K113InfraStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    new NodejsFunction(this, 'fn', {
        entry: path.join(__dirname, '../code/index.js'),
        runtime: Runtime.NODEJS_14_X,
        memorySize: 1024,
      }
    );
  }
}
