import * as cdk from '@aws-cdk/core';
import {Code, Function, Runtime} from '@aws-cdk/aws-lambda';
import {join} from 'path';

export class LgcStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const environment = {
      GOOS: 'linux',
      GOARCH: 'amd64',
    };
    // The code that defines your stack goes here
    new Function(this, 'lgc', {
      runtime: Runtime.GO_1_X,
      handler: 'main',
      code: Code.fromAsset(join(__dirname, '../code'),
        {
          bundling: {
            user: "root",
            image: Runtime.GO_1_X.bundlingDockerImage,
            command: [
              'bash','-c', [
                'go build -mod=mod -o /asset-output/main main/main.go' ,
              ].join(' && '),
            ],
            environment: environment,
          }

        }),
      memorySize: 1024,
    });

  }
}
