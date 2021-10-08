# Atividade Prática - Lógica de Programação e Algoritmos
# Análise e Desenvolvimento de Sistemas - UNINTER
# Autor: Ricardo Motta
# Data: 29/08/2021
# Exercício 2
# Faça uma função que receba nome e sobrenome de uma pessoa e retorne a primeira # letra
# do seu nome e sobrenome concatenando com a string '@algoritmos.com.br'


def cadastro(n, s, r):
    # Docstrings explicando utilidade da função
    """
    -> Mostra na tela o email gerado
    :param n: nome do aluno
    :param s: sobrenome do aluno
    :param r: ru do aluno
    :return: sem retorno
    """
    # Saída dos dados inputados
    mail = (f'Sr(a). {n} {s}, seu email é {(n[0]).lower()}' + s.lower() + (r[-2]) + (r[-1]) +'@algoritmos.com.br')
    print(mail)


# Programa principal com Input de dados
nome = input('Digite seu primeiro nome: ').strip().capitalize()
sobrenome = input('Digite seu último nome: ').strip().capitalize()
ru = str(input('Digite seu RU: '))

# Invocação da função
cadastro(nome, sobrenome, ru)

