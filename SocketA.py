import random
import socket
import json
import time
falha = 1



def matrizmake (texto, quantidade, ordem, min, max, taxa):
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
        time.sleep(1 / taxa)  # serve para fazer testes mais precisos.

        matriz['fim'] = time.time()  # Variavel para registrar o calculo de cada matriz
        tempo_matriz = matriz['fim'] - matriz['inicial']  # Utiliza as variaveis para calcular o tempo passsado para gerar cada matriz
        print(f"\033[1;34mA MATRIZ {contador + 1} foi gerada com {tempo_matriz:.5f} segundos.... \033[m")
        listamatriz.append(matriz.copy())

    return listamatriz


# Funções que farão o envio das matrizes
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = (input("Por favor informe o endereço da Maquina G1 [enter = 192.168.128.2]: "))
if HOST == '':
    HOST = '192.168.128.2'
PORT = int(input("Informe o numero do PORT CRIADO na Maquina G1: "))

while falha:

        try:
            print(f"Tentando conectar ao endereço '{HOST}' pela porta {PORT}")
            s.connect((HOST, PORT))
        except:
            print(f"Endereço '{HOST}' não conectado!!")
            HOST = input("Por favor informe o endereço da Maquina G1 [enter = self]: ")
            if HOST == '':
                HOST = '127.0.0.1'
            PORT = int(input("Informe o numero do PORT CRIADO no Serviço B: "))
            falha = 1
        else:
            print(f"Endereço '{HOST}' conectado!!")
            falha = 0


# VARIAVEIS:
quantidade = int(input("Qual a quantidade de matrizes: ")) # Pergunta ao usuário qual a quantidade de matrizes
ordem = int(input("Informe a ordem da matriz: ")) # Coloca na variavel ordem um inteiro que sera o tamanho da matriz

texto = list() # lista para registar em arquivo as matrizes geradas.
taxa = float(input("Informe a taxa de matrizes por segungo: ")) # Taxa de criação das matrizes [MATRIZES/Segundo]


#Variavel que registra o tempo atual em segundos para calculo do tempo total gasto
ini_total = time.time()

# Função para geração dos valores e registro em uma lista os valores dos elementos em seus respectivos indices
arquivo = matrizmake(texto, quantidade, ordem, min, max, taxa)

#Variavel que registra o tempo atual em segundos para calculo do tempo total gasto
fim_total = time.time()

print(type(arquivo))
print(arquivo)


b = json.dumps(arquivo).encode('utf-8')
s.sendall(b)


#Utiliza as variaveis para calcular o tempo passsado para gerar cada matriz
print(f"\033[1;32mForam geradas {quantidade} matrizes em {fim_total - ini_total:.5f} segundos\033[m")
