from typing import Optional

from aws_cdk import pipelines as pipelines, aws_route53 as route53
from constructs import Construct

from cdk_webapp_skeleton import BranchConfig


class MockBranchConfig(BranchConfig):
    def __init__(self, branch_name: str):
        super(MockBranchConfig, self).__init__(branch_name, domain_name_base="testing.com")

    @property
    def source(self):
        return pipelines.CodePipelineSource.connection("owner/repo", self.branch_name, connection_arn="arn")

    def get_hosted_zone(self, scope: Construct) -> Optional[route53.IHostedZone]:
        return None
