# Aula Prática - Lógica de Programação e Algoritmos
# Análise e Desenvolvimento de Sistemas - UNINTER
# Autor: Ricardo Motta
# Data: 29/08/2021
# Exercício 2 - Cadastro de colecionador de jogos

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nomeArquivo} foi criado com sucesso.')

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cadJogo(nomeArquivo, nomeJogo, nomeConsole):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir arquivo.')
    else:
        a.write(f'{nomeJogo} ; {nomeConsole} \n')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        print(a.read())
    finally:
        a.close()


#Programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado.')
else:
    print('Arquivo inexistente.')
    criaArquivo(arquivo)

while True:
    print("""MENU
            1- Cadastrar novo item;
            2- Listar cadastros;
            3- Sair""")

    op = valida_int('Digite uma opção: ', 1, 3)
    if op == 1:
        print('Opção 1 selecionada')
        nomeJogo = input('Nome do jogo: ')
        nomeConsole = input('Nome console: ')
        cadJogo(arquivo, nomeJogo, nomeConsole)
    elif op == 2:
        print('Opção 2 selecionada')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break