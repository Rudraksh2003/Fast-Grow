variable "aws_region" {
  description = "The AWS region to deploy in"
  type        = string
  default     = "us-west-2"
}

variable "key_name" {
  description = "The name of the SSH key pair to use for the instance"
  type        = string
}

