terraform {
  required_version = ">= 1.8.0"

  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.73.0"
    }
  }

  backend "s3" {
    bucket = "mybucket"
    key = "aws-vm/terraform.tfstate"
    region = "sa-east-1"
  }
}

provider "aws" {
  region = var.region

  default_tags {
    tags = {
      owner = "enterprise-x"
      managed-by = "terraform"
    }
  }
}

data "terraform_remote_state" "vpc" {
  backend = "s3"
  config = {
    bucket = "mybucket"
    key = "aws-vpc/terraform.tfstate"
    region = "sa-east-1"
  }
}
