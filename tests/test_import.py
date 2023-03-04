from cdk_webapp_skeleton import BranchCICDStack
from aws_cdk import (
    pipelines as pipelines,
)


def test_instantiate():
    source = pipelines.CodePipelineSource.connection("owner/repo", "branch", connection_arn="arn")
    BranchCICDStack(None, source=source)
