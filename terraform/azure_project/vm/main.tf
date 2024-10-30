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
    key                  = "azure-vm/terraform.tfstate"
  }

}

provider "azurerm" {
  features {}
}

data "terraform_remote_state" "vnet" {
  backend = "azurerm"
  config = {
    resource_group_name  = "resource_group_terraform"
    storage_account_name = "joaooliveiraterraform"
    container_name       = "remote-state"
    key                  = "azure-vnet/terraform.tfstate"
  }
}
