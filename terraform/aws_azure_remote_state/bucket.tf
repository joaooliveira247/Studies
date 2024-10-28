resource "aws_s3_bucket" "s3" {
  bucket = "joaoolveira-remote-state"
}

resource "aws_s3_bucket_versioning" "s3_versioning" {
  bucket = aws_s3_bucket.s3.id
  versioning_configuration {
    status = "Enable"
  }
}
