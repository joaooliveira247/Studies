output "bucket_id" {
  description = "AWS S3 Bucket ID"
  value       = aws_s3_bucket.bucket.id
}
