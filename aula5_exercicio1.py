def realce(s1):
    print('-' * 10)
    print(s1)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é igual = {s}')


def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')



# realce('*TESTANDO*')
# soma(b= 10, a=50)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
