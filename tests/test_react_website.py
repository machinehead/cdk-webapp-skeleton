from pprint import pprint

import aws_cdk as cdk
from aws_cdk import assertions

from cdk_webapp_skeleton import ReactWebsite

from .mock_branch_config import MockBranchConfig


class ReactWebsiteTestStack(cdk.Stack):
    def __init__(self):
        super().__init__()

        ReactWebsite(self, "ReactWebsite", MockBranchConfig("main"))


def test_react_website():
    template = assertions.Template.from_stack(ReactWebsiteTestStack())
    pprint(template.to_json())

    template.has_resource(
        "AWS::S3::Bucket",
        {
            "Properties": {
                "PublicAccessBlockConfiguration": {
                    "BlockPublicAcls": True,
                    "BlockPublicPolicy": True,
                    "IgnorePublicAcls": True,
                    "RestrictPublicBuckets": True,
                },
                "Tags": [{"Key": "aws-cdk:auto-delete-objects", "Value": "true"}],
            },
            "UpdateReplacePolicy": "Delete",
            "DeletionPolicy": "Delete",
        },
    )
    template.has_resource(
        "AWS::CloudFront::Distribution",
        {
            "Properties": {
                "DistributionConfig": {
                    "Aliases": ["testing.com", "www.testing.com"],
                    "CustomErrorResponses": [
                        {
                            "ErrorCode": 403,
                            "ResponseCode": 200,
                            "ResponsePagePath": "/index.html",
                        },
                        {
                            "ErrorCode": 404,
                            "ResponseCode": 200,
                            "ResponsePagePath": "/index.html",
                        },
                    ],
                    "DefaultCacheBehavior": {
                        "AllowedMethods": ["GET", "HEAD"],
                        "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e58f6",
                        "Compress": True,
                        "ResponseHeadersPolicyId": {
                            "Ref": "FrontendResponseHeadersPolicyB0F64B3D"
                        },
                        "TargetOriginId": "FrontendDistributionOrigin1C335E87B",
                        "ViewerProtocolPolicy": "redirect-to-https",
                    },
                    "DefaultRootObject": "index.html",
                    "Enabled": True,
                    "HttpVersion": "http2",
                    "IPV6Enabled": True,
                    "Origins": [
                        {
                            "DomainName": {
                                "Fn::GetAtt": [
                                    "FrontendBucket5DAC5524",
                                    "RegionalDomainName",
                                ]
                            },
                            "Id": "FrontendDistributionOrigin1C335E87B",
                            "S3OriginConfig": {
                                "OriginAccessIdentity": {
                                    "Fn::Join": [
                                        "",
                                        [
                                            "origin-access-identity/cloudfront/",
                                            {
                                                "Ref": "FrontendDistributionOrigin1S3Origin0C7BC470"
                                            },
                                        ],
                                    ]
                                }
                            },
                        }
                    ],
                    "PriceClass": "PriceClass_100",
                    "ViewerCertificate": {
                        "AcmCertificateArn": {
                            "Fn::GetAtt": [
                                "FrontendCertificateCertificateRequestorResource0EC072BF",
                                "Arn",
                            ]
                        },
                        "MinimumProtocolVersion": "TLSv1.2_2021",
                        "SslSupportMethod": "sni-only",
                    },
                }
            },
        },
    )
