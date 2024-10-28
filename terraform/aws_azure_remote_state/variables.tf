variable "azure_location" {
  description = "Azure Region"
  type        = string
  default     = "Brazil South"
}

variable "azure_account_tier" {
  description = "Azure Account Tier"
  type        = string
  default     = "Standard"
}

variable "azure_replication_type" {
  description = "Azure Replication Type"
  type        = string
  default     = "LRS"
}
