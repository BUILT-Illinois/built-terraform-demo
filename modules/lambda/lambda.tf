data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "${path.module}/../../src"
  output_path = "${path.module}/../../src/lambda_src.zip"
}

resource "aws_lambda_function" "api_lambda" {
  function_name = "tech-committee-demo"
  role          = var.lambda_role_arn
  handler       = "main.lambda_handler"
  runtime       = "python3.13"

  filename         = "${path.module}/../../src/lambda_src.zip"
  source_code_hash = data.archive_file.lambda.output_base64sha256

  timeout     = 10
  memory_size = 128

  environment {
    variables = {
      MY_ENV_VAR = "some_environment_var"
    }
  }
}

resource "aws_lambda_function_url" "example_lambda_url" {
  function_name      = aws_lambda_function.api_lambda.function_name
  authorization_type = "NONE"
}
