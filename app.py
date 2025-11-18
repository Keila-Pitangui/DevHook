import pika
from flask import Flask, request, jsonify

app = Flask(__name__)
RABBITMQ_HOST = 'rabbitmq'  # Ou 'localhost' se rodar localmente

def publish_message(message):
    try:
        # 1. Conexão ao RabbitMQ
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()

        # 2. Declaração da Fila (Certifique-se que ela existe)
        channel.queue_declare(queue='minha_fila_de_testes')

        # 3. Publicação da Mensagem
        channel.basic_publish(
            exchange='',
            routing_key='minha_fila_de_testes',
            body=message.encode('utf-8')
        )
        print(f" [x] Mensagem enviada: {message}")
        connection.close()
        return True
    except Exception as e:
        print(f"Erro ao conectar/enviar ao RabbitMQ: {e}")
        return False

@app.route('/enviar', methods=['POST'])
def send_to_queue():
    data = request.get_json()
    if not data or 'payload' not in data:
        return jsonify({'status': 'erro', 'mensagem': 'Payload ausente'}), 400

    payload = data['payload']
    if publish_message(payload):
        return jsonify({
            'status': 'sucesso',
            'mensagem': 'Requisição recebida e enviada para a fila',
            'dados': payload
        }), 200
    else:
        return jsonify({
            'status': 'erro',
            'mensagem': 'Falha ao enviar mensagem para o RabbitMQ'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)