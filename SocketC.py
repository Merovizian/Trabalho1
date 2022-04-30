import socket
import json
import time
#import numpy as np



# Pergunta ao usuário qual que é o endereço do host e a port (Serviço C é o HOST)
host = (input("Por favor informe o endereço da Maquina G2 [enter = 192.168.128.2]: "))
if host == '':
    host = '192.168.128.2'
port = int(input("Crie uma porta para o Serviço G2 [enter = 6800]: "))
if port == '':
    port = 6800


print("Definindo o servidor ")
time.sleep(0.5)
print("Configurando socket para AFINET E SOCK STREM")
time.sleep(0.5)
SocketB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Fazendo a conexao no endereço {host} e na porta {port}")
time.sleep(0.5)
SocketB.bind((host, port))
SocketB.listen()
print("Servidor Ativo!!")
time.sleep(0.5)

while 1:
    #Programa fica em stand by esperando o client
    print("1 - Esperando a conexão com o Serviço B")
    conexao, endereco = SocketB.accept()
    print(f"2 - Endereço '{endereco}' conectado!! Aguardando Matrizes .....")
    time.sleep(1)
    #Coloca na variavel arquivo a lista de dicionarios que vier do cliente
    arquivo = json.loads(conexao.recv(16384).decode('utf-8'))
    conexao.close()

    #Exibir as matrizes recebidas
    print("3 - Pacotes Recebidos")
    time.sleep(1)
    m = arquivo[0]['quantidade']
    n = arquivo[0]['ordem']

    lista_matrizes = list()
    auxiliar = list()
    auxiliar2 = list()
    tempoagora = time.time()

    resultado = input("Matrizes do Serviço B Recebidas ! deseja exibilas? [N/S]: ")
    while resultado not in ("N, Nao, Sim, S, NAO, SIM, s,n"):
        resultado = input("Opção inválida, por favor digite [N/S]: ")
    print()

    if resultado in ("sim, S, SIM,s"):
        for a in range(0, m):
            print(f"Matriz {a+1}")
            for b in range(0, n):
                print(arquivo[a]['matriz'][b])
            print(f"Det Inversa: {arquivo[a]['inversa']}")
            print(f"Tempo total de execução {arquivo[a]['fim'] - arquivo[a]['inicial']}")
            print()

    else:
        for a in range(0, int(arquivo[0]['quantidade'])):
            print(f"O Determinante da Matriz {a + 1} {arquivo[a]['inversa']}")
            print(f"Tempo total de execução {arquivo[a]['fim'] - arquivo[a]['inicial']}")


    continuacao = input("Deseja fazer mais alguma operação? ")
