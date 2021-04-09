import { expect as expectCDK, matchTemplate, MatchStyle } from '@aws-cdk/assert';
import * as cdk from '@aws-cdk/core';
import * as K95Graph from '../lib/k95-graph-stack';

test('Empty Stack', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new K95Graph.K95GraphStack(app, 'MyTestStack');
    // THEN
    expectCDK(stack).to(matchTemplate({
      "Resources": {}
    }, MatchStyle.EXACT))
});
