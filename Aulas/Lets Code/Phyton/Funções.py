# FUNÇÕES

# Criando funções

#from selectors import EpollSelector


def saudacao():
    print("Seja bem vindo(a)")
    print('Olá, é um prazer ter você fazendo parte desse curso!')

#saudacao()

# função com parâmetro

def saudacao1(nome, curso='Phyton'):
    print(f"Seja bem vindo(a) {nome}")
    print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}!')

saudacao1('Wellington')
saudacao1('wilton',"Java")


# função com retorno

def soma (num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print('O resultado da soma é: ', resultado)


def calculadora(num1, num2, operacao='*'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    else:
        print("ERRO na operação informada")
        print('Informe os dados novamente')
        return

num1 = float(input('Informe o 1º numero: '))
num2 = float(input('Informe o 2º numero: '))
operacao = input('Informa a operação (soma + | menos - | multiplica * | divide /  ')
resultado = calculadora(num1, num2, operacao)

print('O resultado é: ', resultado)