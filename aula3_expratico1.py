v1 = int(input('Digite o primeiro valor inteiro: '))
v2 = int(input('Digite o segundo valor inteiro: '))
v3 = int(input('Digite o último valor inteiro: '))

if (v1 > 0) and (v2 > 0) and (v3 > 0):
    if (v1 + v2 > v3) and (v1 +v3 > v2) and (v2 + v3 > v1):
        if v1 == v2 == v3:
            print('Triângulo equilátero!')
        elif v1 == v2 or v2 == v3 or v3 == v1:
            print('Triangulo Isóceles!')
        elif v1 != v2 and v2 != v3 and v3 != v1:
            print('Triangulo Escaleno')
    else:
        print('Ao menos um dos valores não servem para formar um triângulo')
else:
    print('Ao menos um dos valores não servem para formar um triângulo')
    print(f:teste {} teste {}'. (v1, v2))