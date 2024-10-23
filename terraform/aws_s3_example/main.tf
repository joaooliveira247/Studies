terraform {
  required_version = ">= 1.8.0"
  
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.58.0"
    }
  }
}

provider "aws" {
  region = "sa-east-1"
  // aws tem, azure n
  default_tags {
    tags = {
      owner = "Enterprise-x"
      project = "x"
      managed-by = "terraform"
    }
  }
}