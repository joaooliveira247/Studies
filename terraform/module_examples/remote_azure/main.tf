terraform {
  required_version = ">= 1.8.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.7.0"
    }
  }

  backend "azurerm" {
    resource_group_name  = "resource_group_terraform"
    storage_account_name = "joaooliveiraterraform"
    container_name       = "remote-state"
    key                  = "azure-vm-remote-modules/terraform.tfstate"
  }

}

provider "azurerm" {
  features {}
}

module "network" {
  source = "Azure/network/azurerm"
  version = "5.3.0"

  resource_group_name = azurerm_resource_group.resource_group.name
  use_for_each = true
  subnet_names = ["subnet-${var.enviroment}"]

  tags = local.common_tags

  vnet_name = "vnet-${var.enviroment}"

}
