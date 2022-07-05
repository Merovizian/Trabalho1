# TRABALHO 1  - Laboratório de Redes
por Eric Giobini

## O que é?

São programas para a avaliação da matéria de Laboratório de Redes. 
O objetivo geral é a comunicação entre três máquinas distintas, ou seja, cada um dos programas deverá ser rodado em uma VM diferente.
Cada programa tem uma função específica: 

O programa SocketA.py é o primeiro programa, que deverá gerar matrizes aleatórias com a quantidade e o tamanho sendo informadas pelo usuário.

O programa SocketB.py é o segundo programa, que deverá receber as matrizes enviadas pelo programa 1, inverter cada uma delas e calcular o seu determinante. O resultado dessas manipulações matemáticas em cada matriz é enviado para o programa 3.

O programa SocketC.py deve receber os resultados obtidos no programa 2 e printar na tela do usuário, junto com as informações do tempo total de cada uma das matrizes geradas, desde a criação delas no programa 1.

## Requisitos

-Python3
-3 Máquinas virtuais

### Máquinas virtuais
Obs: Para funcionamento do modo automático de dados, é necessário que as máquinas virtuais sejam:

g2-8 para SocketC.py

g1-8 para SocketB.py

aluno2-7 para SocketA.py
 

## Tutorial
### SocketC


Os programas foram criados para rodar na ordem inversa, ou seja, o primeiro programa a ser rodado é o SocketC.py, não há a necessidade de adicionar atributos neste programa, basta rodá-lo pelo terminal.
~~~
python3 SocketC.py 
~~~
Ao abrir o programa o usuário deverá informar se os parâmetros de conexão com o programa 2 (SocketB.py) serão inseridos manualmente. Caso o usuário não queira inserir os dados, tais como endereço de ip e porta, o próprio programa irá gerar automaticamente os dados necessários para a conexão. 

Após inserir os dados para conexão, o programa ficará ativo, em stand by, esperando a conexão do SocketB.py. 
### SocketB
O próximo passo é abrir o segundo programa.
Em outra máquina virtual o usuário deverá abrir o programa SocketB.py, sem a necessidade de adicionar atributos.
~~~
python3 SocketB.py 
~~~ 
Ao abrir o programa o usuário irá se deparar com a mesma solicitação do programa 3 (SocketC.py), se o programa deve gerar os dados de conexão automaticamente, ou o usuário inserir manualmente os dados. 

Após essa etapa, o programa, assim como o programa 3, permanecerá ativo, em stand by, esperando conexão com o SocketA.py
### SocketA
O último passo tutorial é rodar o primeiro programa. Para isso, em outra máquina virtual 
