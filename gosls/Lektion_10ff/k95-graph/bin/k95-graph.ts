#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { K95GraphStack } from '../lib/k95-graph-stack';

const app = new cdk.App();
new K95GraphStack(app, 'K95GraphStack');
