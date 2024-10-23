resource "aws_s3_bucket" "data_lake_s3" {
  bucket = "my-data-lake-w-tf"
  
  tags = {
    Name = "Test Data Lake"
  }
}