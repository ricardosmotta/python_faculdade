preco = float(input('Informe o preço do produto R$ '))
desc = float(input('Informe o percentual de desconto: '))

percentual = preco * (desc / 100)
final = preco - percentual
print('O valor do desconto é de R$ {} e o preço final será de R$ {}.' .format(percentual, final))
