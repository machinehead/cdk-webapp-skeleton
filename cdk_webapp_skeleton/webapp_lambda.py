from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class WebappLambda(Construct):
    """Assumes a local folder called "webapp-backend" with a Dockerfile in it."""

    def __init__(self, scope: "Construct", _id: str, lambda_runtime_environment=None):
        super().__init__(scope, _id)
        if lambda_runtime_environment is None:
            lambda_runtime_environment = {}

        self.webapp_lambda_func = _lambda.DockerImageFunction(
            scope,
            "FlaskLambda",
            code=_lambda.DockerImageCode.from_image_asset(
                directory="webapp-backend"
            ),
            environment=lambda_runtime_environment
        )
