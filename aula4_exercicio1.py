# escreve um algoritmo que fique recebndo frases ou palavras digitadas pelo usuário
# encerre o algoritmo quando a palavra sair for digitada
print('Digite uma msg. Para encerrar digite "sair".')
frase = ''

while (frase != 'sair'):
    frase = input(' ')
    print(frase)
print('Encerrando programa...')