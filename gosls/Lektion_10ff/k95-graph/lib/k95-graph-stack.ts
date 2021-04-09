import {join} from 'path';
import * as cdk from '@aws-cdk/core';
import { ContentHandling, LambdaIntegration, LambdaRestApi } from '@aws-cdk/aws-apigateway';
import { CfnOutput, DockerImage } from '@aws-cdk/core';
import { Effect, PolicyStatement } from '@aws-cdk/aws-iam'
import {Code, Function, Runtime} from '@aws-cdk/aws-lambda';


export class K95GraphStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const environment = {
      GOOS: 'linux',
      GOARCH: 'amd64',
    };
    
    // Ich verwende GO 1.16 features, das wird im Standart Bundling nicht unterstützt
    const image = DockerImage.fromRegistry("golang:latest")
    const backend=new Function(this, 'lgc', {
      runtime: Runtime.GO_1_X,
      handler: 'main',
      code: Code.fromAsset(join(__dirname, '../code'),
        {
          bundling: {
            user: "root",
            //image: Runtime.GO_1_X.bundlingDockerImage,
            image,
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
    // Accountnummer anpassen
    backend.addToRolePolicy(
      new PolicyStatement(
        {
          effect: Effect.ALLOW,
          actions: [
            "dynamodb:Scan"          
          ],
          resources: [
            "arn:aws:dynamodb:eu-central-1:123456789012:table/daily-weight"]
        }
      )
    )

    const api = new LambdaRestApi(this, 'chart', {
      binaryMediaTypes: ["image/png","text/html"],
      deploy: true,
      handler: backend,
      proxy: false,
    });
    
    const lambdaIntegration = new LambdaIntegration(backend, {
      contentHandling: ContentHandling.CONVERT_TO_BINARY,
      
    });

    const items = api.root.addResource('image');
    items.addMethod('GET',lambdaIntegration);  // GET /items
    
    
    new CfnOutput(this, "url",
    {
      value: api.url+"image"
    })
  }
}
