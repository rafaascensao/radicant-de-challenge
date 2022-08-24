terraform {
    required_version = ">= 1.1.3, < 2.0.0"

    backend "s3" {
        bucket = "rafaascensao-terraform-state"
        key    = "radicant-de-challenge/terraform.tfstate"
        region = "eu-west-1"
    }

    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 3.72"
        }
    }
}

provider "aws" {
    region = "eu-west-1"
}