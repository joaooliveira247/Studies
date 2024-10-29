variable "location" {
  description = "Azure Location"
  type        = string
  default     = "Brazil South"
}

variable "account_tier" {
  description = "Azure Account Tier"
  type        = string
  default     = "Standard"
}

variable "replication_type" {
  description = "Azure Replication Type"
  type        = string
  default     = "LRS"
}
