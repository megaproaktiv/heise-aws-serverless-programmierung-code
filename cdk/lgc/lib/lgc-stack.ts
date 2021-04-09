import * as cdk from '@aws-cdk/core';
import {Code, Function, Runtime} from '@aws-cdk/aws-lambda';
import {join} from 'path';

export class LgcStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    new Function(this, 'lgc', {
      runtime: Runtime.GO_1_X,
      handler: 'lambda',
      code: Code.fromAsset(join(__dirname, '../dist')),
      memorySize: 1024,
    });

  }
}
