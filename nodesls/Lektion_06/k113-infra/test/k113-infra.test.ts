import { expect as expectCDK, matchTemplate, MatchStyle } from '@aws-cdk/assert';
import * as cdk from '@aws-cdk/core';
import * as K113Infra from '../lib/k113-infra-stack';

test('Empty Stack', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new K113Infra.K113InfraStack(app, 'MyTestStack');
    // THEN
    expectCDK(stack).to(matchTemplate({
      "Resources": {}
    }, MatchStyle.EXACT))
});
