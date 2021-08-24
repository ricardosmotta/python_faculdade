# nota = 0
#
# while nota >= 0 and nota <= 10:
#     aluno = input('Nome do aluno: ')
#     nota = float(input('Nota final: '))
#     if (nota >= 0) and (nota <= 2.9):
#         print('O aluno {} tirou nota {} e se enquadra no conceito E.'.format(aluno, nota))
#     elif (nota >= 3) and (nota <= 4.9):
#         print('O aluno {} tirou nota {} e se enquadra no conceito D.'.format(aluno, nota))
#     elif (nota >= 5) and (nota <= 6.9):
#         print('O aluno {} tirou nota {} e se enquadra no conceito C.'.format(aluno, nota))
#     elif (nota >= 7) and (nota <= 8.9):
#         print('O aluno {} tirou nota {} e se enquadra no conceito B.'.format(aluno, nota))
#     elif (nota >= 9) and (nota <= 10):
#         print('O aluno {} tirou nota {} e se enquadra no conceito A.'.format(aluno, nota))
#     else:
#         print('A nota digitada é inválida. Encerrando programa...')


# Exercício 1 - Laço de repetição
while True:
    # input dos dados
    aluno = input('Nome do aluno: ').capitalize()                                                 # capitalize -> coloca a primeira letra em maiúscula
    nota = float(input('Nota final: '))                                                           # float -> números decimais

    # condicionais e saída de dados
    if (nota >= 0) and (nota <= 2.9):
        print('O aluno {} tirou nota {} e se enquadra no conceito E.'.format(aluno, nota))
    elif (nota >= 3) and (nota <= 4.9):
        print('O aluno {} tirou nota {} e se enquadra no conceito D.'.format(aluno, nota))
    elif (nota >= 5) and (nota <= 6.9):
        print('O aluno {} tirou nota {} e se enquadra no conceito C.'.format(aluno, nota))
    elif (nota >= 7) and (nota <= 8.9):
        print('O aluno {} tirou nota {} e se enquadra no conceito B.'.format(aluno, nota))
    elif (nota >= 9) and (nota <= 10):
        print('O aluno {} tirou nota {} e se enquadra no conceito A.'.format(aluno, nota))
    else:
        if nota <= 0 or nota >= 10:
            print('A nota digitada é inválida. Encerrando programa...')
            break                                                                                 # break -> condição de parada do algoritmo