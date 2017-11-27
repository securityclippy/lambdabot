module "api_gateway" {
  source = "../../modules/api_gateway"
  aws_profile = "${var.aws_profile}"
  lambda_bot_name = "${var.lambda_bot_name}"
}