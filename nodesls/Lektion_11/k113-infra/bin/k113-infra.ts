#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { K113InfraStack } from '../lib/k113-infra-stack';
import { K113WebsiteStack } from '../lib/k113-website';

const app = new cdk.App();
new K113InfraStack(app, 'K113InfraStack');
new K113WebsiteStack(app, 'K113WebsiteStack');
