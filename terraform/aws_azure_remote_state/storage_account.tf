resource "azurerm_resource_group" "resource_group" {
  name     = "testetf"
  location = var.azure_location

  tags = local.common_tags
}

resource "azurerm_storage_account" "storage_account" {
  name                     = "joaooliveiraterraform"
  account_replication_type = var.azure_replication_type
  account_tier             = var.azure_account_tier
  location                 = azurerm_resource_group.resource_group.location
  resource_group_name      = azurerm_resource_group.resource_group.name
  
  blob_properties {
    versioning_enabled = true
  }

  tags = local.common_tags
}

resource "azurerm_storage_container" "container" {
  name                  = "remote-state"
  storage_account_name  = azurerm_storage_account.storage_account.name
  container_access_type = "private"
}
