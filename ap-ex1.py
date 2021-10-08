# Atividade Prática - Lógica de Programação e Algoritmos
# Análise e Desenvolvimento de Sistemas - UNINTER
# Autor: Ricardo Motta
# Data: 29/08/2021
# Exercício 1
# Algoritmo que recebe o nome de um aluno e sua nota e informa em qual conceito ele se enquadra.

# Laço de repetição
while True:
    print('*** PARA ENCERRAR DIGITE: "SAIR" ***')
    aluno = input('Nome do aluno: ').upper()

    # Condição de encerramento
    if aluno == 'SAIR':
        print('~' * 25)
        print('Encerrando programa...')
        break

    # Condição de enquadramento das notas mostrando saída
    else:
        nota = float(input('Nota final: '))
        if (nota >= 0) and (nota <= 2.9):
            print(f'O aluno {aluno} tirou nota {nota:0.1f} e se enquadra no conceito E.')
        elif (nota >= 3) and (nota <= 4.9):
            print(f'O aluno {aluno} tirou nota {nota:0.1f} e se enquadra no conceito D.')
        elif (nota >= 5) and (nota <= 6.9):
            print(f'O aluno {aluno} tirou nota {nota:0.1f} e se enquadra no conceito C.')
        elif (nota >= 7) and (nota <= 8.9):
            print(f'O aluno {aluno} tirou nota {nota:0.1f} e se enquadra no conceito B.')
        elif (nota >= 9) and (nota <= 10):
            print(f'O aluno {aluno} tirou nota {nota:0.1f} e se enquadra no conceito A.')
        else:
            # Condição de encerramento se entrada for inválida
            if nota <= 0 or nota >= 10:
                print('~' * 30)
                print('A nota digitada é inválida.\nEncerrando programa...')
                print('~' * 30)
                break