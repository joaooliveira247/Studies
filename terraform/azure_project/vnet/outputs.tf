output "subnet-id" {
  description = "Azure Subnet ID"
  value       = azurerm_subnet.subnet.id
}

output "security_group_id" {
  description = "Azure Security Group ID"
  value       = azurerm_network_security_group.network_security_group.id
}
