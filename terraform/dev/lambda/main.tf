module "lambda" {
  source = "../../modules/lambda"
  aws_profile = "${var.aws_profile}"
  lambda_bot_name = "${var.lambda_bot_name}"
}