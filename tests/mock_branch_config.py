from typing import Optional

from aws_cdk import aws_route53 as route53
from aws_cdk import pipelines as pipelines
from constructs import Construct

from cdk_webapp_skeleton import BranchConfig


class MockBranchConfig(BranchConfig):
    def __init__(self, branch_name: str):
        super(MockBranchConfig, self).__init__(branch_name)

    @property
    def domain_name_base(self) -> Optional[str]:
        return "testing.com"

    @property
    def source(self):
        return pipelines.CodePipelineSource.connection(
            "owner/repo", self.branch_name, connection_arn="arn"
        )

    def get_hosted_zone(self, scope: Construct) -> Optional[route53.IHostedZone]:
        return route53.HostedZone.from_hosted_zone_attributes(
            scope,
            f"HostedZone_{self.domain_name_base}",
            hosted_zone_id="RANDOMHZID",
            zone_name=self.domain_name_base,
        )
