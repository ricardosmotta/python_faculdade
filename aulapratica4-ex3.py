somavalor = 0
totpessoas = 0
somaidade = 0

while True:
    idade = (input('Digite sua idade: '))
    if idade == 'sair':
        break
    idade = int(idade)
    somaidade += idade
    totpessoas += 1
    if idade < 3:
        print('O ingresso é gratuíto para menores de 3 anos.')
        somavalor += 0
    elif 3 <= idade <= 12:
        print('O ingresso custa R$ 15,00 para crianças de 3 a 12 anos.')
        somavalor += 15
    elif idade > 12:
        print('Maiores de 12 anos pagam R$ 30,00 pelo ingresso.')
        somavalor += 30
print({:=^40})
print(f'O total de pessoas que compraram ingressos foi de {totpessoas} pessoas.')
print(f'O valor total de dinheiro arrecadado foi R$ {somavalor:.2f}.')
print(f'E a média de idade da galera foi de {somaidade/totpessoas:.0f} anos.')