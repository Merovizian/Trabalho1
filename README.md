# TRABALHO 1  - Laboratório de Redes
por Eric Giobini

## O que é?

São programas para a avaliação da matéria de Laboratório de Redes. 
O objetivo geral é a comunicação entre três máquinas distintas, ou seja, cada um dos programas deverá ser rodado em uma VM diferente.
Cada programa tem uma função específica: 

O programa SocketA.py é o primeiro programa, que deverá gerar matrizes aleatórias com a quantidade e o tamanho sendo informadas pelo usuário.

O programa SocketB.py é o segundo programa, que deverá receber as matrizes enviadas pelo programa 1, inverter cada uma delas e calcular o seu determinante. O resultado dessas manipulações matemáticas em cada matriz é enviado para o programa 3.

O programa SocketC.py é o terceiro progradoisma, que receberá os resultados obtidos no programa 2 e printar na tela do usuário, junto com as informações do tempo total de cada uma das matrizes geradas, desde a criação delas no programa 1.

## Requisitos

- Python3

- Máquinas virtuais

### Máquinas virtuais

Para funcionamento do modo automático de dados, é necessário que as máquinas virtuais sejam:


**g2-8** para SocketC.py

**g1-8** para SocketB.py

**aluno2-7** para SocketA.py

 

## Tutorial
### SocketC


Os programas foram criados para rodar na ordem inversa, ou seja, o primeiro programa a ser rodado é o SocketC.py, não há a necessidade de adicionar atributos neste programa, basta rodá-lo pelo terminal.
~~~
python3 SocketC.py 
~~~
Ao abrir o programa o usuário deverá informar se os parâmetros de conexão com o programa 2 (SocketB.py) serão inseridos manualmente. Caso o usuário não queira inserir os dados, tais como endereço de ip e porta, o próprio programa irá gerar automaticamente os dados necessários para a conexão (Lembre-se: para funcionamento do modo automático, os requisitos deverão ser satisfeitos). 

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
O último passo tutorial é rodar o primeiro programa. Para isso, em outra máquina virtual o usuário deve abrir o programa 1.
~~~
python3 SocketA.py 
~~~ 
Ao abrir o programa, será apresentado os mesmos atributos ao usuário, referentes a conexão automática.
Se a conexão foi concluída com sucesso, o SocketB irá atualizar seu status para “2 - [...]” e irá retornar os dados de conexão com o SocketA, como IP e a Porta. assim como um aviso de que está aguardando as Matrizes. 

O usuário, então, deverá inserir os dados referente às características sobre as Matrizes, como a quantidade e a ordem.


## Funcionalidade

Assim que terminar o tutorial acima, o programa 1 irá enviar as matrizes para o programa 2, e retornará para o usuário os seguintes dados: tempo de criação de cada matriz, tempo geral de criação de todas as matrizes e se o usuário gostaria de imprimir as matrizes na tela. Também será informado sobre a possibilidade de gerar novamente matrizes, mas essa funcionalidade é beta.

O programa 1 é finalizado e não têm mais utilidade, as matrizes geradas estão no programa dois. O programa 2 assim que receber solicitação de conexão do programa 1 irá apresentar os dados dessa conexão como IP e Porta, fará os cálculos dos determinantes e a inversa.

Assim que terminar os cálculos, o programa 2 se conectará com o programa 3 e enviará as matrizes juntamente com os resultados dos cálculos. 
O programa 3 mostrará os dados da conexão com o programa 2 como IP e Porta e retornará para o usuário o tempo de cada matriz do programa 1 até este ponto. Há a opção de apresentar mais dados, como tempo de cada matriz, cada uma das matrizes, determinante, caso o usuário queira.

IMPORTANTE: Existe uma limitação no tamanho dos dados a serem enviados pelos programas. Sendo recomendado criar no máximo 80 matrizes, de ordem máxima 10.


## Problemas

O programa foi projetado para evitar erros, e caso ocorram, há uma interatividade com o usuário orientando sobre o que deve ser feito. Caso um dos programas apresente uma situação não esperada, basta finalizar a aplicação (ctrl + c) e abri-la novamente.

## Feedback

Caso tenha alguma dúvida, sugestão ou tenha encontrado algum erro, por favor mande um email para ericgmicaela@gmail.com

## Referencias
[HOW TO sobre Programação de  soquetes](https://docs.python.org/pt-br/3/howto/sockets.html)
[Python3 Documentation](https://www.python.org/doc/)
[NumPy documentation](https://numpy.org/doc/stable/)


