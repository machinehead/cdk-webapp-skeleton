import aws_cdk as cdk
from aws_cdk import assertions

from cdk_webapp_skeleton import WebappLambda

from .mock_branch_config import MockBranchConfig


class WebappLambdaTestStack(cdk.Stack):
    def __init__(self):
        super().__init__()

        WebappLambda(
            self,
            "WebappLambda",
            MockBranchConfig("main"),
            image_directory="tests/lambda_image",
        )


def test_webapp_lambda():
    template = assertions.Template.from_stack(WebappLambdaTestStack())
    template.resource_count_is("AWS::Lambda::Function", 2)
    template.has_resource(
        "AWS::Lambda::Function",
        {
            "Properties": {
                "PackageType": "Image",
            }
        },
    )
    template.resource_count_is("AWS::CloudWatch::Alarm", 1)
    template.resource_count_is("AWS::Logs::MetricFilter", 1)
