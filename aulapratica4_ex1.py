op = input('Qual operação você deseja realizar? + , - , * ou / : ')

if (op == '+') or (op == '-') or (op == '*') or (op == '/'):
    v1 = int(input('Digite um valor inteiro: '))
    v2 = int(input('Digite outro valor inteiro: '))



while op != 's':
    if (op == '+'):
        res = v1 + v2
        print('Resultado da soma entre {} e {} é: {}'.format(v1, v2, res))
    elif (op == '-'):
        res = v1 - v2
        print('Resultado da subtração entre {} e {} é: {}'.format(v1, v2, res))
    elif (op == '*'):
        res = v1 * v2
        print('Resultado da multiplicação entre {} e {} é: {}'.format(v1, v2, res))
    elif (op == '/'):
        res = v1 / v2
        print('Resultado da divisão entre {} e {} é: {:.2f}'.format(v1, v2, res))
    else:
        print('Opção inválida.')

    op = input('Qual operação você deseja realizar? + , - , * ou / : ')
    if (op == '+') or (op == '-') or (op == '*') or (op == '/'):
        v1 = int(input('Digite um valor inteiro: '))
        v2 = int(input('Digite outro valor inteiro: '))
print('Encerrando programa...')