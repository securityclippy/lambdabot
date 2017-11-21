module "lambda" {
  source = "../../modules/lambda"
  aws_profile = "${var.aws_profile}"
}