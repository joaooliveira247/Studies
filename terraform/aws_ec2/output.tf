output "vm_ip" {
  description = "AWS EC2 IP"
  value = aws_instance.vm.public_ip
}