# 1. Provedores
terraform {
  required_providers {
    rabbitmq = {
      source  = "cyrilgdn/rabbitmq"
      version = "~> 1.22"
    }
  }
}

provider "rabbitmq" {
  endpoint = "http://localhost:15672" 
  username = "guest"                
  password = "guest"                 
}

