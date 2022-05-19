# hashtag indica que a linha é comentario

"""
quando usamos 3 aspas também é considerado comentário,
sendo iniciado e terminado o trecho de comentário por 3 """


# função para imprimir na tela
print('Hello World!')
print('Bem vindo ao curso de Python!')

# imprime mensagem na tela e aguarda entrada de dados
# input('Qual linguagem vc está estudando?')

# Variáveis

idade = 26 # o Python define automoticamente o tipo da variável, que neste caso é int (inteiro)

nome = "Wellington"

altura = 1,85

estudante = True

array = nome, idade, altura, estudante

print(idade) # imprime o conteudo da variável
print(type(idade)) # imprime o tipo da variável
print(type(nome))
print(type(altura))
print(type(estudante))
print(type(array))


print(nome, " - ", idade, " - ", altura, " - ", estudante)

# como capturar o valor informado pelo usuário em variável
linguagem = input('Qual linguagem vc está estudando?')

print("A liguagem que voce está estudando é ", linguagem)

print(array)

