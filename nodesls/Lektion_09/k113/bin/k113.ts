#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { K113Stack } from '../lib/k113-stack';

const app = new cdk.App();
new K113Stack(app, 'K113Stack');
