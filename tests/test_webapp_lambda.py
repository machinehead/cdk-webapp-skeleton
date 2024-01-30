import aws_cdk as cdk
from aws_cdk import assertions
from aws_cdk import aws_lambda as _lambda

from cdk_webapp_skeleton import WebappLambda

from .mock_branch_config import MockBranchConfig


class WebappLambdaTestStack(cdk.Stack):
    def __init__(self):
        super().__init__()

        WebappLambda(
            self,
            "WebappLambda",
            MockBranchConfig("main"),
            code=_lambda.DockerImageCode.from_image_asset(
                directory="tests/lambda_image"
            ),
            timeout=cdk.Duration.seconds(4),
            enable_profiling=False,
            enable_alarms=True,
        )


def test_webapp_lambda(snapshot):
    template = assertions.Template.from_stack(WebappLambdaTestStack())
    assert template.to_json() == snapshot
