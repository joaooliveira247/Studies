terraform {
  required_version = ">= 1.8.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.73.0"
    }
  }

  backend "s3" {
    // you can create bucket to save state before
    bucket = "example-bucket"
    key    = "aws-vpc/terraform.tfstate"
    region = "sa-east-1"
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      owner      = "enterprise-x"
      managed-by = "terraform"
    }
  }
}
