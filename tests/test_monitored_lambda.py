import aws_cdk as cdk
import pytest
from aws_cdk import assertions
from aws_cdk import aws_lambda as _lambda

from cdk_webapp_skeleton import MonitoredLambdaFunction


class MonitoredLambdaTestStack(cdk.Stack):
    def __init__(self, *, enable_profiling: bool = True, enable_alarms: bool = True):
        super().__init__()

        MonitoredLambdaFunction(
            self,
            "MonitoredLambda",
            code=_lambda.DockerImageCode.from_image_asset(
                directory="tests/lambda_image"
            ),
            timeout=cdk.Duration.seconds(4),
            enable_profiling=enable_profiling,
            enable_alarms=enable_alarms,
        )


@pytest.mark.parametrize(
    "enable_profiling,enable_alarms",
    [(False, False), (False, True), (True, False), (True, True)],
)
def test_monitored_lambda(snapshot, enable_profiling, enable_alarms):
    template = assertions.Template.from_stack(
        MonitoredLambdaTestStack(
            enable_profiling=enable_profiling, enable_alarms=enable_alarms
        )
    )
    assert template.to_json() == snapshot
