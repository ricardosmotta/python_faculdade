# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# if nome == 'Ricardo':
#     print('O nome digitado foi {}.'.format(nome))
# elif idade < 18:
#     print('Você é menor de idade e não pode acessar esse programa.')
# elif idade > 100:
#     print('Você chegou longe e tá fazendo hora extra.')
# else:
#     print('PROGRAMA ENCERRADO!')

x = 2
y = 5
z = 0
resultado = 0
valor = int(input('Digite 1 ,2 ou 3: '))

if (valor == 1):
    resultado = x * valor
    valor = 2

if (valor == 2):
    resultado += y
    valor = 3

if (valor == 3):
    resultado += z

print(resultado)
