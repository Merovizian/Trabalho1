import socket
import json
import time
import numpy as np

#import numpy as np
falha = 1



# Pergunta ao usuário qual que é o endereço do host e a port (Serviço C é o HOST)
automatica = input("Deseja inserir dados manualmente? ")
while automatica.lower() not in ('n','s','sim','nao'):
    automatica = input("Opção inválida, por favor digite [N/S]: ")
print()

if automatica in ("sim, S, SIM,s"):
    host = (input("Por favor informe o endereço desta Maquina (G1) [enter = 192.168.128.66]: "))
    if host == '':
        host = '192.168.128.66'
    port = (input("Crie uma porta para o Serviço G2 [enter = 6800]: "))
    if port == '':
        port = 6800
    else:
        port = int(port)
else:
    host = '192.168.128.66'
    port = 6800



'''while falha:

    try:
        print(f"Tentando conectar ao endereço '{host}' pela porta {port}")
        SocketB.connect((host, port))
    except:
        print(f"Endereço '{host}' não conectado!!")
        host = (input("Por favor informe o endereço desta Maquina (G1) [enter = 192.168.128.66]: "))
        if host == '':
            host = '192.168.128.66'
        port = (input("Crie uma porta para o Serviço G2 [enter = 6800]: "))
        if port == '':
            port = 6800
        falha = 1
    else:
        print(f"Endereço '{host}' conectado!!")
        falha = 0'''


SocketB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    print("1 - Esperando a conexão com a Maquina G2")
    conexao, endereco = SocketB.accept()
    print(f"2 - Endereço '{endereco}' conectado!! Aguardando Matrizes .....")
    time.sleep(1)
    #Coloca na variavel arquivo a lista de dicionarios que vier do cliente
    arquivo = json.loads(conexao.recv(16384).decode('utf-8'))
    conexao.close()

    #Exibir as matrizes recebidas
    print("3 - Pacotes Recebidos")
    tempofinal = time.time()
    print(f"TEMPO DA CRIAÇÃO ATÉ RECEBIMENTO DE MATRIZES: {round(time.time() - arquivo[0]['inicial'],2)}")

    m = arquivo[0]['quantidade']
    n = arquivo[0]['ordem']

    lista_matrizes = list()
    auxiliar = list()
    auxiliar2 = list()
    tempoagora = time.time()

    resultado = input("Matrizes da Maquina G2 recebidas! deseja exibilas? [N/S]: ")
    while resultado not in ("N, Nao, Sim, S, NAO, SIM, s,n"):
        resultado = input("Opção inválida, por favor digite [N/S]: ")
    print()

    '''   if resultado in ("sim, S, SIM,s"):
        for a in range(0, m):
            print(f"Matriz {a+1}")
            print(arquivo[a]['matriz'])
#            print(numpy.linalg.inv(arquivo[a]['matriz']))
            print(f"Det Inversa: {arquivo[a]['inversa']}")
            print(f"Tempo total de execução {round(time.time() - arquivo[a]['inicial'],2)} segundos")
            print()'''

    if resultado in ("sim, S, SIM,s"):
        for a in range(0, m):
            print(f"Matriz {a+1}")
            for b in range(0, n):
                print(arquivo[a]['matriz'][b])
            print(f"Det: {round(np.linalg.det(arquivo[a]['matriz']), 5)}")
            print(f"Det Inversa: {arquivo[a]['inversa']}")



    else:
        for a in range(0, int(arquivo[0]['quantidade'])):
            print(f"O Determinante da Inversa da Matriz {a + 1}: {round(arquivo[a]['inversa'],5)}")
            print(f"Tempo total de da Matriz {a+1}: {round(tempofinal - arquivo[a]['inicial'],2)} segundos")
    print()
    print(f"TEMPO DE EXECUÇAO TOTAL DESTE PROGRAMA: {round(time.time() - arquivo[0]['inicial'],2)} segundos")
    break
    #caso queira implementar algo mais.
    #continuacao = input("Deseja fazer mais alguma operação? ")