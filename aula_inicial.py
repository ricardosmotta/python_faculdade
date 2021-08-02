a = 1
b = 5

resposta = a == b

print(resposta)

resposta = a != b
print(resposta)

type(resposta)
print(type, resposta)

frase = 'Olá, mundo!'
print(frase[5])

v1 = 'Des'
v1 = v1 + 'coordenador'
print(v1)

nota = 0
v1 = 'Você é um cordenador nota %.2f e um péssimo profissional' % nota
print(v1)

nota = 0
curso = 'ADS'
v1 = 'Você, coordenador de {} e merece nota {} pela falta de profissionalismo'.format(curso, nota)
print(v1)
tamanho = len(v1)
print(tamanho)

burro = input('Escreva o nome do pior coordenador da uninter: ')
jegue = burro
print('Eu, {}, sou muito imbecil'.format(burro))

nota = float(input('Qual nota você dá para a coordenação? '))
print('O coordenador de ADS tirou nota {}.'.format(nota))
