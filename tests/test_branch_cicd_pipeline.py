import aws_cdk as cdk
import pytest

from cdk_webapp_skeleton import BranchCICDPipeline, BranchConfig
from aws_cdk import (
    pipelines as pipelines,
    assertions,
)


@pytest.fixture
def testing_branch_config():
    class TestingBranchConfig(BranchConfig):
        def __init__(self, branch_name: str):
            super(TestingBranchConfig, self).__init__(branch_name, domain_name_base="testing.com")

        @property
        def source(self):
            return pipelines.CodePipelineSource.connection("owner/repo", self.branch_name, connection_arn="arn")

    return TestingBranchConfig.from_branch_name("main")


def test_branch_cicd_pipeline(testing_branch_config: BranchConfig):
    app = cdk.App()
    stack = cdk.Stack(app, "CICDStack")
    BranchCICDPipeline(stack, testing_branch_config)
    template = assertions.Template.from_stack(stack)

    # PipelineArtifactsBucket
    # CacheBucket
    template.resource_count_is("AWS::S3::Bucket", 2)

    template.resource_count_is("AWS::CodePipeline::Pipeline", 1)
