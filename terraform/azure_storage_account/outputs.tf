output "storage_account_id" {
  description = "Azure Storage Account ID"
  value       = azurerm_storage_account.storage_account.id
}

output "sa_primary_access_key" {
  description = "Azure Storage Account Primary Acess Key"
  value       = azurerm_storage_account.storage_account.primary_access_key
  sensitive   = true
}