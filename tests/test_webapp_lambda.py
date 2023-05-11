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
        )


def test_webapp_lambda():
    template = assertions.Template.from_stack(WebappLambdaTestStack())
    # pprint(template.to_json())
    template.resource_count_is("AWS::Lambda::Function", 2)
    template.has_resource(
        "AWS::Lambda::Function",
        {
            "Properties": {
                "PackageType": "Image",
            }
        },
    )
    template.resource_count_is("AWS::CloudWatch::Alarm", 2)
    template.resource_count_is("AWS::Logs::MetricFilter", 1)
    # FlaskLambda warmup rule
    template.has_resource(
        "AWS::Events::Rule",
        {
            "Properties": {
                "ScheduleExpression": "rate(1 minute)",
                "Targets": [
                    {
                        "HttpParameters": {},
                        "Id": "Target0",
                        # Make sure that if the lambda fails, a retry storm doesn't happen
                        "RetryPolicy": {"MaximumRetryAttempts": 0},
                    }
                ],
            },
        },
    )
