import { expect as expectCDK,   haveResource } from '@aws-cdk/assert';
import * as cdk from '@aws-cdk/core';
import * as K113 from '../lib/k113-stack';

test('Empty Stack', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new K113.K113Stack(app, 'MyTestStack');
    // THEN
    expectCDK(stack).to(haveResource("AWS::Lambda::Function"));
}
)
