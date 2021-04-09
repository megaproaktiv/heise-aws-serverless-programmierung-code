import { expect as expectCDK,  haveResource, ResourcePart } from '@aws-cdk/assert';
import * as cdk from '@aws-cdk/core';
import * as K113Infra from '../lib/k113-infra-stack';

test('Lambda Stack', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new K113Infra.K113InfraStack(app, 'MyTestStack');
    // THEN
    expectCDK(stack).to(haveResource("AWS::Lambda::Function"));
    expectCDK(stack).to(haveResource("AWS::ApiGateway::RestApi"));
}
);
