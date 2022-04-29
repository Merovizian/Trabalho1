import socket
import json
import time
import numpy as np
falha = 1


# Pergunta ao usuário qual que é o endereço do host e a port (Serviço B é o HOST)


host = (input("Por favor informe o endereço do Serviço B [enter = self]: "))
if host == '':
	host = '127.0.0.1'
port = int(input("Crie uma porta para o Serviço A: "))


print("Definindo o servidor")
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
    print("1 - Esperando a conexão com o Serviço A")
    conexao, endereco = SocketB.accept()
    print(f"2 - Endereço '{endereco}' conectado!! Aguardando Matrizes .....")
    time.sleep(1)
    #Coloca na variavel arquivo a lista de dicionarios que vier do cliente
    arquivo = json.loads(conexao.recv(16384).decode('utf-8'))
    conexao.close()

    print("3 - Pacotes Recebidos")
    time.sleep(1)
    m = arquivo[0]['quantidade']
    n = arquivo[0]['ordem']
    print(f"Foram recebidas {m} Matrizes de Ordem {n} x {n}")
    auxiliar = list()
    auxiliar2 = list()
    tempoagora = time.time()

    #Cria a lista das 'm' matrizes e as coloca na variavel lista_matrizes
    for b in range(0, arquivo[0]['quantidade']):
        print(f"Tempo da Matriz {b}: {round(tempoagora - arquivo[b]['fim'],3)} segundos")
        time.sleep(0.5)
        for a in arquivo[b]['matriz']:
            if a == '\n':
                auxiliar2.append(auxiliar.copy())
                auxiliar.clear()
            if a in ('0,1,2,3,4,5,6,7,8,9'):
                auxiliar.append(int(a))
        arquivo[b]['matriz'] = auxiliar2.copy()
        auxiliar2.clear()

        #Cria uma key inversa na listas de dicionarios.
        arquivo[b]['inversa'] = round(1 / np.linalg.det(arquivo[b]['matriz']), 5)
    print()

    print("Pacote Recebido com Sucesso!! ")



    # Envio das matrizes
    HOST2 = (input("Por favor informar o endereço do Serviço C [enter = self]: "))
    if HOST2 == '':
        HOST2 = '127.0.0.1'
    PORT2 = int(input("Informe o numero do PORT CRIADO no Serviço C: "))

    SocketC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while falha:

        try:
            print(f"Tentando conectar ao endereço '{HOST2}' pela porta {PORT2}")
            SocketC.connect((HOST2, PORT2))
        except:
            print(f"Endereço '{HOST2}' não conectado!!")
            HOST2 = input("Por favor informe o endereço do Serviço C [enter = self]: ")
            if HOST2 == '':
                HOST2 = '127.0.0.1'
            PORT2 = int(input("Informe o numero do PORT CRIADO no Serviço C: "))
            falha = 1
        else:
            print(f"Endereço '{HOST2}' conectado!!")
            falha = 0


    SocketC.send(json.dumps(arquivo).encode('utf-8'))

    continuacao = input("Deseja fazer mais alguma operação? ")


