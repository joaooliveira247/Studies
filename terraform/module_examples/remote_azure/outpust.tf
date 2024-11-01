output "vm_ip" {
  description = "Azure Virtual Machine IP"
  value       = azurerm_linux_virtual_machine.vm.public_ip_address
}