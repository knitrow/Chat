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

# Criar socket do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen(1)

print(f"Servidor aguardando conexão em {HOST}:{PORT}...")

# Aceitar conexão do cliente
conexao, endereco = servidor.accept()
print(f"Conectado com {endereco}")

# Verificar se há mensagem inicial via sys.argv
if len(sys.argv) > 1:
    mensagem_inicial = " ".join(sys.argv[1:])
    conexao.send(mensagem_inicial.encode())
    print(f"Eu: {mensagem_inicial}")

# Loop principal para troca de mensagens
while True:
    # Receber mensagem do cliente
    try:
        mensagem_recebida = conexao.recv(1024).decode()
        if mensagem_recebida:
            print(f"Cliente: {mensagem_recebida}")
        else:
            print("Cliente desconectado.")
            break
    except:
        print("Erro ou cliente desconectado.")
        break

    # Enviar mensagem para o cliente
    mensagem = input("Eu: ")
    conexao.send(mensagem.encode())

# Fechar conexão
conexao.close()
servidor.close()