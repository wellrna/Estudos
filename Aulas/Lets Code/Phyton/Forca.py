"""
Jogo da Forca - Autor: Benedeto
Construí o codigo permitindo a escolha do assunto: GERAL ou PYTHON
A palavra é sorteada no dicionário escolhido: GERAL ou PYTHON
Se o significado for preenchido no dicionario,
este é apresentado no final do jogo
"""

# '----------INICIO exercicio DESAFIO Python----------'

import random
import os
from socket import NI_NOFQDN
from time import sleep

os.system('cls')
nome = input('Olá! Qual é o seu nome ? ')
print(' ')

os.system('cls')
print('Olá,', nome, '!', 'Seja bem-vinda(o) ao Jogo da Forca!')
print(' ')

# '----------INICIO função DESAFIO Python----------'
def sorteia_palavra():
    dicionario_python = {
    'int':'tipo de variavel - números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000',
    'float':'tipo de variavel - números reais, ou seja, números com parte decimal: 1.0, -7.7,1.14',
    'str':'tipo de variavel - cadeia de caracteres, ou seja, dados textuais',
    'bool':'tipo de variavel - valores lógicos (booleanos) True ou False',
    'print':'uma função para imprimir alguma coisa na tela',
    'input':'uma função para receber informação pelo teclado',
    'type':'uma função obter o tipo da variável',
    'identação':'é o espaçamento aplicado no inicio das linhas do código',
    'booleanos':'valores lógicos (tipo de variavel: bool) True ou False'}

    dicionario_geral = {
    'CADEIRA':'',
    'TELHADO':'',
    'ARMARIO':'',
    'BICICLETA':'',
    'RESTAURANTE':''}

    tema = ''
    while tema == '':
        assunto = input('Escolha um assunto: Geral (G), Python (P)')
        if assunto.upper() == 'G' or assunto.upper() == 'GERAL' :
            tema = assunto.upper()
            palavra = random.choice(list(dicionario_geral.keys()))
            significado = dicionario_geral[palavra]
        elif assunto.upper() == 'P' or assunto.upper() == 'PHYTON' :
            tema = assunto.upper()
            palavra = random.choice(list(dicionario_python.keys()))
            significado = dicionario_python[palavra]
        else:
            print('***', assunto, ' inválido ***')
    return palavra,significado
# '----------FIM DE função DESAFIO Python----------'

deseja_jogar = 'S'
while deseja_jogar == 'S':
    letras_erradas = ''

    palavra,significado = sorteia_palavra()
    os.system('cls')
    print(' ')
    print('Sua palavra tem ', len(palavra), 'letras.')

    lista_palavra = list(palavra) # converte os digitos da palavra em uma lista
    lista_montagem = []
    lista_escolhidas = []

    for i in range(len(lista_palavra)):
        lista_montagem.append('_')

    print(' ')
    input('Pressione qualquer tecla para começar o jogo ')
    mensagem_alerta = 'Você só pode errar 6 vezes até acertar a palavra!'
    mensagem = ''
    mensagem_letra_sim = ''
    mensagem_letra_nao = ''
    total_acertos = 0
    total_erros = 0
    fim = ''
    while fim == '':
        os.system('cls')
        if mensagem_letra_sim != '':
            print(mensagem_letra_sim)
        print(' ')
        montada_aux = ''
        for i in range(len(lista_montagem)):
            montada_aux = ' ' + montada_aux + lista_montagem[i] + ' '
        print(montada_aux)
        print(' ')
        if mensagem_letra_nao != '':
            print(mensagem_letra_nao)

        if letras_erradas != '':
            print('Letras erradas:', letras_erradas)
        print(' ')

        if total_acertos == len(palavra):
            print('P a r a b é n s , você acertou a palavra')
            print('A palavra é [', palavra, ']', significado)
            fim = 'S'
        if total_erros >= 6:
            print('* * * Você errou 6 vezes * * *')
            print('A palavra é [', palavra, ']', significado)
            fim = 'S'

        if fim == 'S':
            print(' ')
            deseja_jogar = (input('Deseja jogar novamente (S/N)')).upper()
            os.system('cls')

        if fim == '':

            print(' ')
            print(mensagem_alerta)   

            letra_escolhida = input('Escolha uma letra: ')
            erro_ja_escolhida = 0
            for i in range(len(lista_escolhidas)):
                if lista_escolhidas[i].upper() == letra_escolhida.upper():
                    erro_ja_escolhida = 1
            if erro_ja_escolhida == 1:
                mensagem_alerta = '[' + letra_escolhida.upper() + '], ### Essa letra ja foi escolhida, tente outra! ###'
            else:
                lista_escolhidas.append(letra_escolhida.upper())
                total_encontradas = 0
                mensagem_alerta = ''
                mensagem_letra_sim = ''
                mensagem_letra_nao = ''
                for i in range(len(lista_palavra)):
                    if lista_palavra[i].upper() == letra_escolhida.upper():
                        mensagem_letra_sim = 'Muito bom! essa letra existe na sua palavra!'
                        lista_montagem[i] = letra_escolhida.upper()
                        total_encontradas = total_encontradas + 1
                if total_encontradas == 0:
                    letras_erradas = letras_erradas + letra_escolhida.upper()
                    mensagem_letra_nao = 'Oh! essa letra não existe na sua palavra!'
                    total_erros = total_erros + 1
                else:
                    total_acertos = total_acertos + total_encontradas
                if total_encontradas > 1:
                    mensagem_letra_sim = 'Uau! essa letra existe na sua palavra!'


# '----------FIM DE exercicio DESAFIO Python----------'