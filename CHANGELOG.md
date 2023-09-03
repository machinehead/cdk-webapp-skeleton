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
