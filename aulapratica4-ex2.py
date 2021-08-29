valor = int(input('Digite o valor que deseja sacar R$ '))

while True:
    if valor >= 100:
        ced100 = valor // 100
        valor -= ced100 * 100
        print(f'Cédulas de 100: {ced100}')
        if not valor:
            break
    if valor >= 50:
        ced50 = valor // 50
        valor -= ced50 * 50
        print(f'Cédulas de 50: {ced50}')
        if not valor:
            break
    if valor >= 20:
        ced20 = valor // 20
        valor -= ced20 * 20
        print(f'Cédulas de 20: {ced20}')
        if not valor:
            break
    if valor >= 10:
        ced10 = valor // 10
        valor -= ced10 * 10
        print(f'Cédulas de 10: {ced10}')
        if not valor:
            break
    if valor >= 5:
        ced5 = valor // 5
        valor -= ced5 * 5
        print(f'Cédulas de 5: {ced5}')
        if not valor:
            break
    if valor >= 1:
        ced1 = valor
        print(f'Cédulas de 1: {ced1}')
        break