terraform {
  required_version = ">= 1.8.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.74.0"
    }
  }

  backend "aws" {
    backend "s3" {
        bucket = "mybucket"
        key = "aws-vm/terraform.tfstate"
        region = "sa-east-1"
      }
    }
  }
}

module "s3_bucket" {
  source      = "./modules/s3_bucket"
  bucket_name = "my-unique-bucket-name"
}

provider "aws" {
  region = var.location
}
