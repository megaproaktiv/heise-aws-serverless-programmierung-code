#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { K96InfraStack } from '../lib/k96-infra-stack';

const app = new cdk.App();
new K96InfraStack(app, 'K96InfraStack');
