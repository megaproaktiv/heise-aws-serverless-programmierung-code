#!/usr/bin/env python3

from aws_cdk import core

from lpc.lpc_stack import LpcStack


app = core.App()
LpcStack(app, "lpc")

app.synth()
