print('[ 1 ] Maçã')
print('[ 2 ] Laranja')
print('[ 3 ] Banana')

prod = int(input('Qual dos produtos acima você deseja? '))


while prod != 1 and prod != 2 and prod != 3:
    print('Escolha um valor válido!!!')
    prod = int(input('Qual dos produtos acima você deseja? '))
    if prod == 1 or prod == 2 or prod == 3:
        qtde = int(input('Qual a quantidade: '))
    if prod == 1:
        pagar = qtde * 2.30
        print('Você comprou {} maçãs e o total a pagar é R${}'.format(qtde, pagar))
    else:
        if prod == 2:
            pagar = qtde * 3.50
            print('Você comprou {} laranjas e o total a pagar é R${}'.format(qtde, pagar))
        else:
            if prod == 3:
                pagar = qtde * 1.99
                print('Você comprou {} bananas e o total a pagar é R${}'.format(qtde, pagar))
