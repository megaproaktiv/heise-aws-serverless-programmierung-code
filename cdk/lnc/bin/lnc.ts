#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { LncStack } from '../lib/lnc-stack';

const app = new cdk.App();
new LncStack(app, 'LncStack');
