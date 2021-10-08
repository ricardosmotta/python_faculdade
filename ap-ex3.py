# Atividade Prática - Lógica de Programação e Algoritmos
# Análise e Desenvolvimento de Sistemas - UNINTER
# Autor: Ricardo Motta
# Data: 29/08/2021
# Exercício 3
# Faça um algoritmo que cadastre o nome de pessoas e um valor de doação. O programa deverá embaralhar a lista e sortear
# um ganhador imprimindo seu nome.
# A cada R$ 10,00 doados o nome da pessoa é inserido 1 vez na lista.

# Importação de bibliotecas e criação de listas
import random
from time import sleep
listaSorteio = []
ganhador = []

# Função
def titulo(txt):
    tam = len(txt) + 4
    print('=' * tam)
    print(f'  {txt}')
    print('=' * tam)

# Cabeçalho do programa
titulo('FAÇA UMA DOAÇÃO E CONCORRA A UM PRÊMIO SURPRESA')
titulo('A CADA R$ 10,00 VOCÊ TEM UMA CHANCE A MAIS')

# Programa Principal
while True:
    # Input de dados
    querDoar = input('Quer fazer uma doação? [S/N]: ').strip().upper()

    # Condição de encerramento
    if querDoar == 'N':
        print('Encerrando programa... Efetuando o sorteio...')
        break
    # Condição para cálculos
    else:
        nome = input('Digite seu nome: ').capitalize()
        valor = int(input('Digite valor de sua doação R$ '))
        valor = valor // 10
        listaSorteio += [nome] * valor

# Comandos para sorteio
random.shuffle(listaSorteio)
ganhador = random.choice(listaSorteio)

# Comando sleep para simular o sorteio
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')

# Resultado do sorteio aproveitando a função criada
titulo('E o nome sorteado foi... ' + ganhador + '!!! Parabéns!!!')
titulo(f'Lista de sorteados: {listaSorteio}')




