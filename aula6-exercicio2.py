#Jogo Jokenpo (Pedra, Papel e Tesoura)
from random import randint

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x


def vencedor(j1, j2):
    global empate, v1, v2
    if j1 == 1:         # Pedra
        if j2 == 1:     # Pedra
            empate += 1
        elif j2 == 2:   # Papel
            v2 += 1
        elif j2 == 3:    # Tesoura
            v1 += 1
    elif j1 == 2:       # Papel
        if j2 == 1:     # Pedra
            v1 +=1
        elif j2 == 2:   # Papel
            empate += 1
        elif j2 == 3:    # Tesoura
            v2 += 1
    elif j1 == 3:       # Tesoura
        if j2 == 1:     # Pedra
            v2 += 1
        elif j2 == 2:   # Papel
            v1 += 1
        elif j2 == 3:    # Tesoura
            empate += 1
    resultados = [v1, v2, empate]
    return resultados


print('~'*20)
print('      JOKENPO    ')
print('~'*20)
print("""1- Pedra
2- Papel
3- Tesoura""")
print('~'*20)

resultados = []
jogadas = []
v1 = v2 = empate = 0

while True:
    p1 = valida_int('Escolha sua jogada: ', 0, 3)
    if p1 == 0:
        break
    p2 = randint(1, 3)
    jogadas.append([p1, p2])
    resultados = vencedor(p1, p2)
    # print(vencedor(p1, p2))

    for jog in jogadas:
        for dado in jog:
            print(dado, end=' ')
        print()

print(f'Número de vitorias do jogador 1: {resultados[0]}')
print(f'Número de vitorias do jogador 2: {resultados[1]}')
print(f'Número de Empates: {resultados[1]}')

