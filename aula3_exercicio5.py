nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
if nome == 'Ricardo':
    print('O nome digitado foi {}.'.format(nome))
elif idade < 18:
    print('Você é menor de idade e não pode acessar esse programa.')
elif idade > 100:
    print('Você chegou longe e tá fazendo hora extra.')
else:
    print('PROGRAMA ENCERRADO!')
