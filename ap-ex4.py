

tabela = {'Código':[], 'Estoque': [], 'Mínimo':[]}

while True:
    codigo = int(input('Digite o código [0 Para Encerrar]: '))
    if codigo == 0:
        print('~' * 30)
        print('    Encerrando programa...')
        print('~' * 30)
        break
    estoque = int(input('Informe a quantidade em estoque: '))
    minimo = int(input('Informe estoque mínimo: '))

    tabela['Código'].append(codigo)
    tabela['Estoque'].append(estoque)
    tabela['Mínimo'].append((minimo))

for c, v in tabela.items():
    print(f'{c}     ', end='')
    for

print()
print(tabela)