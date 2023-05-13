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
