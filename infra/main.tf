resource "aws_s3_bucket" "test" {
  bucket = "rafaascensao-test-one-tf"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}