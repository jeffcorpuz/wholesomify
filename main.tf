resource "aws_iam_role" "wholesomify_lambda" {
  name = "wholesomify_iam"

  assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Effect": "Allow",
            "Sid": ""
        }
    ]
}
EOF
}

resource "aws_lambda_function" "wholesomify_lambda" {
  filename      = "lambda_function.zip"
  function_name = "wholesomify"
  role          = "${aws_iam_role.wholesomify_lambda.arn}"
  handler       = "lambda_handler"

  # The filebase64sha256() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
  # source_code_hash = "${base64sha256(file("lambda_function_payload.zip"))}"
  source_code_hash = "${filebase64sha256("lambda_function.zip")}"

  runtime = "python3.8"

  environment {
    variables = {
      REDDITNAME = "blank",
      PASSWORD   = "blank",
      APPID      = "blank",
      SECRET     = "blank",
      APPNAME    = "blank",
      LIMIT      = "blank"
    }
  }
}
