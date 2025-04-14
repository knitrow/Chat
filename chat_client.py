import socket
import sys

# Função para ler configurações do arquivo config.txt
def ler_config():
    config = {}
    with open("config.txt", "r") as file:
        for linha in file:
            chave, valor = linha.strip().split("=")
            config[chave] = valor
    return config

# Configurações
config = ler_config()
HOST = config["HOST"]
PORT = int(config["PORT"])

# Criar socket do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))
print(f"Conectado ao servidor {HOST}:{PORT}")

# Verificar se há mensagem inicial via sys.argv
if len(sys.argv) > 1:
    mensagem_inicial = " ".join(sys.argv[1:])
    cliente.send(mensagem_inicial.encode())
    print(f"Eu: {mensagem_inicial}")

# Loop principal para troca de mensagens
while True:
    # Receber mensagem do servidor
    try:
        mensagem_recebida = cliente.recv(1024).decode()
        if mensagem_recebida:
            print(f"Servidor: {mensagem_recebida}")
        else:
            print("Servidor desconectado.")
            break
    except:
        print("Erro ou servidor desconectado.")
        break

    # Enviar mensagem para o servidor
    mensagem = input("Eu: ")
    cliente.send(mensagem.encode())

# Fechar conexão
cliente.close()