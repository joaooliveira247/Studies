output "subnet-id" {
  description = "AWS Subnet ID"
  value       = aws_subnet.subnet.id
}

output "security_group_id" {
  description = "Security group ID"
  value       = aws_security_group.security_group.id
}
