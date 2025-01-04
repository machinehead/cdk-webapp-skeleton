## v0.9.10 (2025-01-03)

### Fix

- **branch_cicd_pipeline**: set publish_assets_in_parallel=True [skip ci]

## v0.9.9 (2025-01-03)

### Fix

- **branch_cicd_pipeline**: add Docker credentials for ECR repo [skip ci]

## v0.9.8 (2025-01-03)

### Fix

- **branch_cicd_pipeline**: provide CodeBuild with ecr:GetRepositoryPolicy, ecr:ListImages and ecr:DescribeImages permissions [skip ci]

## v0.9.7 (2025-01-03)

### Fix

- **branch_cicd_pipeline**: provide CodeBuild with ecr:DescribeRepositories permission [skip ci]

## v0.9.6 (2025-01-03)

### Fix

- **branch_cicd_pipeline**: provide CodeBuild with permissions to pull images from ECR
- **react_website**: set IndexDocument on WebsiteBucket to index.html

## v0.9.5 (2024-07-14)

### Fix

- **react_website**: fix typo in 'worker-src' in CloudFront's CSP

## v0.9.4 (2024-07-14)

### Fix

- **react_website**: add 'blob:' to 'worker-src' in CloudFront's CSP to enable Sentry

## v0.9.3 (2024-07-14)

### Fix

- **react_website**: add '*.sentry.io' to 'connect-src' in CloudFront's CSP to enable Sentry

## v0.9.2 (2024-07-04)

### Fix

- **react_website**: add 'unsafe-inline' to script-src in CloudFront's CSP

## v0.9.1 (2024-05-27)

### Fix

- **branch_config**: use the to-be-deprecated property for redirect urls

## v0.9.0 (2024-05-27)

### Feat

- **branch_config**: deprecate dev_signin_redirect_url and add signin_redirect_urls to allow for an arbitrary number of redirect URLs

### Fix

- **branch_config**: try py3.8-compatible list typing

## v0.8.0 (2024-03-31)

### Feat

- **branch_config**: make dev signin URL configurable

## v0.7.1 (2024-03-23)

### Fix

- **react_website**: change Content-Security-Policy to add script-src 'unsafe-eval'

## v0.7.0 (2024-01-30)

### Feat

- **MonitoredLambdaFunction**: add ability to explicitly disable/enable profiling and alarms
- **WebappLambda**: allow specifying the VPC as a parameter
- **AuthStack**: add creating a Google Identity Provider

### Fix

- **MonitoredLambdaFunction**: remove log_retention and migrate to explicitly specifying log group
- **AuthStack**: provide access to Google's email and openid
- **WebappLambda**: fix typing to be compatible with python 3.8
- **MonitoredLambdaFunction**: fix typing to be compatible with python 3.8
- **MonitoredLambdaFunction**: set the RUNNING_IN_AWS=true env var
- **BranchCICDPipeline**: allow the Synth step to perform elasticloadbalancing:DescribeRules

## v0.6.0 (2023-09-10)

### Feat

- **webapp_lambda**: allow specifying the Lambda timeout externally

### Fix

- **WebappLambda**: wrap the hosted zone into the construct's scope
- **SynthStep**: allow the Synth step to perform lookups
- **react_website**: allow loading images from data: by CSP
- **auth_stack**: increase access token validity to 1 day and refresh token to 30 days

## v0.5.1 (2023-09-03)

### Fix

- **BranchCICDPipeline**: move build image to Standard 7 to support Python 3.11

## v0.5.0 (2023-09-03)

### Feat

- **lambdas**: enable passing alarm_topic to subscribe to alarms via SNS
- **BranchCICDPipeline**: send email notifications about execution state change

### Fix

- **BranchCICDPipeline**: create custom artifacts bucket so that it gets deleted on pipeline deletion
- **BranchCICDPipeline**: update the scope of the AlarmTopic to match the rest of resources
- **WebsiteDeployStep**: fix incorrect assignment of type as default value to env_from_cfn_outputs

## v0.4.0 (2023-05-12)

### Feat

- **MonitoredLambdaFunction**: create an alarm tracking Lambda timeouts

### Fix

- **MonitoredLambdaFunction**: change TimeoutsAlarm name back to Timeouts
- **MonitoredLambdaFunction**: rename Timeouts alarm so that the names don't clash with MetricFilter
- **MonitoredLambdaFunction**: change alarms to maintain state upon missing data

## v0.3.1 (2023-05-10)

### Fix

- **webapp_lambda.py**: correctly emitting warnings about image_directory

### Refactor

- **webapp_lambda.py**: clean up duplicate warnings

## v0.3.0 (2023-05-10)
