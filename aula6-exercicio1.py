
words = ('telefone', 'amauri', 'bicicleta', 'celular', 'montanha')

for p in words:
    print(f'\nPalavra: {p.upper()}. Vogais: ', end=' ')
    for l in p:
        if l.lower() not in 'aeiou':
            print(l.upper(), end=' ')
