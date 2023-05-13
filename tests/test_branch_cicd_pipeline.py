import aws_cdk as cdk
import pytest
from aws_cdk import assertions

from cdk_webapp_skeleton import BranchCICDPipeline, BranchConfig

from .mock_branch_config import MockBranchConfig


@pytest.fixture()
def testing_branch_config():
    return MockBranchConfig.from_branch_name("main")


def test_branch_cicd_pipeline(testing_branch_config: BranchConfig):
    app = cdk.App()
    stack = cdk.Stack(app, "CICDStack")
    pipeline = BranchCICDPipeline(stack, testing_branch_config)
    pipeline.build_pipeline()
    template = assertions.Template.from_stack(stack)

    # PipelineArtifactsBucket
    # CacheBucket
    template.resource_count_is("AWS::S3::Bucket", 2)

    template.resource_count_is("AWS::CodePipeline::Pipeline", 1)
