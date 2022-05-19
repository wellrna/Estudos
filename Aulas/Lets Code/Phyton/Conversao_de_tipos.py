#CONVERSÂO DE TIPOS

idade = '26'
num1 = '10'
num2 = '20'

print(idade, type(idade))

idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

 # int () - converte para int
 # str () - converte para str
 # float () - converte para float
 # bool () - converte para bool

# input sempre lê o dado informado como str
altura = input('Informe sua altura: ')

print(altura, type(altura))

# para se ter a informação no tipo correto é preciso fazer a conversão

altura4 = float(input('Informe a sua altura: '))

print(altura4, type(altura4))