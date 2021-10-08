# def parangaricu():
#     palavra1 = 'parangaricu'
#     tirimirruaro(palavra1)
#
# def tirimirruaro(palavra):
#     palavra2 = palavra + 'tirimirruaro'
#     # print(palavra2)
#
# parangaricu()
# print(palavra2)

# for i in range(7, 26,3):
#     print(i)

# for i in range(10, 20):
#     for j in range(10, 20, 2):
#         print(f'{i} + {j} = {i + j}')

# x = int(input('digite um avlor no intevalo de -100 até 100: '))
# while x > 1000 or x < 100:
#     x = int(input('digite um avlor no intevalo de -100 até 100: '))
# print('encerrando...')


# def comida():
#     ovos = 12
#     bacon()
#     print(ovos)
#
# def bacon():
#     ovos = 6
#     print(ovos)
#
#
# comida()

# def valida_int(pergunta, min, max):
#     x = int(input(pergunta))
#     while ((x < min) or (x > max)):
#         x = int(input(pergunta))
#     return x


# def fatorial(num=1):
#     """
#     Cálculo de fatorial
#     :param num: número digitado por usuário
#     :return: o cálculo do fatorial
#     """
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
# x = valida_int('Digite um valor para calcular seu fatorial: ', 0, 999)
# print(f'{x}! = {fatorial(x)}')


# mochila = ('machado', 'camisa', 'abacate', 'lentilha')
# for item in mochila:
#     print(f'Na minha mochila eu tenho {item}.')

# mochila = ['machado', 'camisa', 'abacate', 'ovos', 'lentilha']
# print(mochila)
# mochila.pop(0)
# print(mochila)

# x = [1, 3, 5, 7, 9]
# y = x
# print(x)
# print(y)
#
# x[0] = 0
# print(x)
# print(y)

# def div2(num, den):
#     res = num / den
#     print(res)
#
# div2(3, 10)

# i = 88
# while (i >= 0):
#     print(i)
#     i -= 4

# num = [1, 3, 5, 7, 9]
# num[2] = 11
# num.append(13)
# num.pop()
# num.sort(reverse=True)
# num.insert(1, 1)
# if 10 in num:
#     num.remove(10)
# else:
#     print('Não achei o número 10')
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')

# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
#
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}')

notas = [9, 8, 7, 2, 7, 0, 3, 4, 6, 2, 5]
print(notas)
print(f'A nota 7 consta {notas.count(7)} vezes na lista.')
cont = 0
notas[-1] = 4
print(f'Última nota alterada para {notas[-1]}.')
print(notas)
for r, n in enumerate(notas):
    if n == 4:
        cont += 1
print(f'A nota 4 consta {cont} vezes na lista.')

print(f'Maior nota é {max(notas)}.')
notas.sort()
print(f'Lista em ordem crescente é: {notas}.')
notas.sort(reverse=True)
print(f'Lista em ordem crescente é: {notas}.')
soma = 0
for s in notas:
    soma += s
print(f'A soma dos valores da lista é {soma}.')