import random
import socket
import json
import time

falha = 1



#Pergunta ao usuario se quer inserir os dados de conexao manualmente
automatica = input("Deseja inserir dados de conexao manualmente? ")
while automatica.lower() not in ('n','s','sim','nao'):
    automatica = input("Opção inválida, por favor digite [N/S]: ")


def matrizmake(quantidade, ordem):
    matriz = dict()
    listamatriz = list()
    texto = list()
    for contador in range(0, quantidade):
        matriz['inicial'] = time.time()  # Variavel para registrar o calculo de cada matriz
        matriz['ordem'] = ordem
        matriz['quantidade'] = quantidade
        for x in range(0, ordem):
            for y in range(0, ordem):
                numero = random.randint(0, 9)
                texto.append(f'{numero:0>{len(str(9))}}')
            texto.append('\n')
        matriz['matriz'] = texto.copy()
        texto.clear()
        print(f"\033[1;34mA MATRIZ {contador + 1} foi gerada com {time.time()-matriz['inicial']:.5f} segundos.... \033[m")
        listamatriz.append(matriz.copy())

    return listamatriz


# Funções que farão o envio das matrizes
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if automatica in ("sim, S, SIM,s"):
    HOST = (input("Por favor informe o endereço da Maquina G1 [enter = 192.168.128.2]: "))
    if HOST == '':
        HOST = '192.168.128.2'
    PORT = (input("Informe o numero do PORT CRIADO na Maquina G1 [enter = 5800]: "))
    if PORT == '':
        PORT = 5800
    else:
        port = int(PORT)
else:
    HOST = '192.168.128.2'
    PORT = 5800

while falha:

    try:
        print(f"Tentando conectar ao endereço '{HOST}' pela porta {PORT}  INICIO DO TRY")
        tcp.connect((HOST, PORT))
        ''' VARIAVEIS:  '''
        quantidade = int(input("Qual a quantidade de matrizes: "))  # Pergunta ao usuário qual a quantidade de matrizes
        ordem = int(
            input("Informe a ordem da matriz: "))  # Coloca na variavel ordem um inteiro que sera o tamanho da matriz
        # texto = list()  # lista para registar em arquivo as matrizes geradas.

        # Variavel que registra o tempo atual em segundos para calculo do tempo total gasto
        ini_total = time.time()

        # Função para geração dos valores e registro em uma lista os valores dos elementos em seus respectivos indices
        arquivo = matrizmake(quantidade, ordem)

        # Variavel que registra o tempo atual em segundos para calculo do tempo total gasto
        fim_total = time.time()

        m = arquivo[0]['quantidade']
        n = arquivo[0]['ordem']

        b = json.dumps(arquivo).encode('utf-8')
        tcp.sendall(b)
        tcp.close()

        # Utiliza as variaveis para calcular o tempo passsado para gerar cada matriz
        print(f"\033[1;32mForam geradas {quantidade} matrizes em {fim_total - ini_total:.5f} segundos\033[m")

        # IMPRIME AS MATRIZES
        resultado = input("Deseja imprimir as matrizes? ")
        while resultado not in ("N, Nao, Sim, S, NAO, SIM, s,n"):
            resultado = input("Opção inválida, por favor digite [N/S]: ")
        print()
        m = arquivo[0]['quantidade']
        n = arquivo[0]['ordem']
        print(f"Foram recebidas {m} Matrizes de Ordem {n} x {n}")
        auxiliar = list()
        auxiliar2 = list()
        for b in range(0, arquivo[0]['quantidade']):
            for a in arquivo[b]['matriz']:
                if a == '\n':
                    auxiliar2.append(auxiliar.copy())
                    auxiliar.clear()
                if a in ('0,1,2,3,4,5,6,7,8,9'):
                    auxiliar.append(int(a))
            arquivo[b]['matriz'] = auxiliar2.copy()
            auxiliar2.clear()

        if resultado in ("sim, S, SIM,s"):
            for a in range(0, m):
                print(f"Matriz {a + 1}")
                for b in range(0, n):
                    print(arquivo[a]['matriz'][b])
        opcao = input("Deseja mandar outros arquivos? [S/N] ")
        while opcao not in ("N, Nao, Sim, S, NAO, SIM, s,n"):
            opcao = input("Opção inválida, por favor digite [N/S]: ")
        if opcao in ("sim, S, SIM,s"):
            falha = 1
        else:
            falha = 0

    except:
        tcp.close()
        print(f"Endereço '{HOST}' não conectado!!")
        HOST = (input("Por favor informe o endereço da Maquina G1 [enter = 192.168.128.2]: "))
        if HOST == '':
            HOST = '192.168.128.2'
        PORT = (input("Informe o numero do PORT CRIADO na Maquina G1 [enter = 5800]: "))
        if PORT == '':
            PORT = 5800
        else:
            port = int(PORT)

        falha = 1
    else:
        print()
