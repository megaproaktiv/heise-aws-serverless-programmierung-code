from aws_cdk import core
import aws_cdk.aws_lambda as lambda_
from aws_cdk.aws_lambda_python import PythonFunction

class LpcStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        PythonFunction(self, "lpc",
            entry="code", 
            runtime=lambda_.Runtime.PYTHON_3_6
        )

