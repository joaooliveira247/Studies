output "bucket_id" {
  description = "AWS s3 bucket ID"
  value       = aws_s3_bucket.bucket.id
}

output "bucker_arn" {
  description = "AWS s3 bucket ARN"
  value       = aws_s3_bucket.bucket.arn
}
