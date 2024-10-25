variable "location" {
  type        = string
  description = "Azure Resouces Location"
  default     = "Brazil South"
}

variable "account_tier" {
  description = "Azure Storage Account Tier"
  type        = string
  default     = "Standard"
}

variable "account_replication_type" {
  description = "Storage Account Replication Type"
  type        = string
  default     = "LRS"
}

variable "resource_group_name" {
  description = "Azure Resource Group Name"
  type        = string
  default     = "teste-tf"
}

variable "storage_account_name" {
  description = "Azure Storage Account Name"
  type        = string
  default     = "joaooliveiraterraform"
}

variable "container_name" {
  description = "Azure Container Name"
  type        = string
  default     = "container-tf"
}