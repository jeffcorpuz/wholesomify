# Reddit - Slack - AWS Lambda Integration

### Goals
- Integrate with Reddit's API
- Print out random wholesome post
- Send to Slack using WebHook through AWS Lambda

# Instructions
- Package Python Payload for Lambda
```
zip -r9 ${OLDPWD}/function.zip .
cd $OLDPWD
zip -g function.zip lambda_function.py
```
- Run `terraform apply` to bring up infrastructure on AWS
- Configure Slack Commands with Slack Commands Plugin

# Notes
```
aws lambda update-function-code --function-name my-function --zip-file fileb://function.zip
```
