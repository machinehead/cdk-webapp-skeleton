import aws_cdk as cdk
import pytest
from aws_cdk import (
    assertions
)

from cdk_webapp_skeleton import AuthStack
from cdk_webapp_skeleton.test_utils import print_template, get_branch_name_from_mark
from .mock_branch_config import MockBranchConfig

MAIN_BRANCH_NAME = "main"
FEATURE_BRANCH_NAME = "feature"


@pytest.fixture
def auth_stack(request):
    app = cdk.App()
    branch_name = get_branch_name_from_mark(request)
    return AuthStack(app, MockBranchConfig.from_branch_name(branch_name), user_pool_name="test-userpool")


@pytest.mark.branch_name(MAIN_BRANCH_NAME)
def test_auth_stack_main(auth_stack):
    template = assertions.Template.from_stack(auth_stack)
    template.has_resource(
        "AWS::Cognito::UserPool",
        {
            "Properties": {
                "UserPoolName": "test-userpool",
            },
            "DeletionPolicy": "Retain",
        }
    )
    template.resource_count_is("AWS::Cognito::UserPoolDomain", 0)
    template.has_resource(
        "AWS::Cognito::UserPoolClient",
        {
            "Properties": {
                "CallbackURLs": ["http://localhost:3000/signin", f"https://testing.com/signin"],
            },
        }
    )


@pytest.mark.branch_name(FEATURE_BRANCH_NAME)
def test_auth_stack_feature(auth_stack):
    template = assertions.Template.from_stack(auth_stack)
    print_template(template)
    template.resource_count_is("AWS::Cognito::UserPool", 0)
    template.resource_count_is("AWS::Cognito::UserPoolDomain", 0)
    template.has_resource(
        "AWS::Cognito::UserPoolClient",
        {
            "Properties": {
                "CallbackURLs": ["http://localhost:3000/signin", f"https://{FEATURE_BRANCH_NAME}.testing.com/signin"],
            },
        }
    )
