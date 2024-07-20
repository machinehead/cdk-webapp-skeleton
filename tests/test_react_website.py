from pprint import pprint

import aws_cdk as cdk
from aws_cdk import assertions

from cdk_webapp_skeleton import ReactWebsite, WebsiteDeployStep

from .mock_branch_config import MockBranchConfig


class ReactWebsiteTestStack(cdk.Stack):
    def __init__(self):
        super().__init__()


def test_react_website(snapshot):
    test_stack = ReactWebsiteTestStack()
    ReactWebsite(test_stack, "ReactWebsite", MockBranchConfig("main"))
    template = assertions.Template.from_stack(test_stack)
    assert template.to_json() == snapshot


def test_website_deploy_step():
    test_stack = ReactWebsiteTestStack()
    WebsiteDeployStep(
        test_stack,
        "WebsiteDeployStep",
        MockBranchConfig("main"),
        commands=["test command"],
    )
    template = assertions.Template.from_stack(test_stack)
    pprint(template.to_json())
    # Nothing to assert really
