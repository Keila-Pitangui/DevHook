# 3. Recurso: Criação da Fila
resource "rabbitmq_queue" "app_queue" {
  name  = var.queue_name
  vhost = "/" # Vhost padrão
}

# 4. (Opcional) Recurso: Criação de um Exchange (ponto de troca)
resource "rabbitmq_exchange" "app_exchange" {
  name = var.exchange_name
  type = "direct"
  vhost = "/"
}

# 5. (Opcional) Recurso: Ligação (Binding) entre Fila e Exchange
resource "rabbitmq_binding" "app_binding" {
  source      = rabbitmq_exchange.app_exchange.name
  destination = rabbitmq_queue.app_queue.name
  routing_key = var.queue_name
}