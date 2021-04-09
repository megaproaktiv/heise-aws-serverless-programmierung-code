#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { K113InfraStack } from '../lib/k113-infra-stack';

const app = new cdk.App();
new K113InfraStack(app, 'K113InfraStack');
