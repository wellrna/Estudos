# Listas (Array / Objeto)

notas = [7.9, 9.7, 8.2]

# Criando listas - formas de criar listas vazias
lista = []
lista1 = list()
lista = [52, 'Wellington', 3.1415, True]
listas_de_listas = [1, [51, 62, 73], 4]

print('p1a: ',lista[0])
print('p1b: ',lista[-1]) # em Python indices negativos significa selecionar do última posição para o começo da lista

print('p2a: ',listas_de_listas[0])
print('p2b: ',listas_de_listas[1][0])
print('p2c: ',listas_de_listas[1][2])
print('p2d: ',listas_de_listas[1])
print('p2e: ',listas_de_listas[-1]) # em Python indices negativos significa selecionar do última posição para o começo da lista

lista1 = [10, 50, 30, 40, 25, 60, 5, 1, 51, 62, 73, 4]

#slice

print('p3: ',lista1[0:3]) # a partir da posição 0 imprime até o elemento anterior a posição 3
print('p4: ',lista1[3:6]) # a partir da posição 3 imprime até o elemento anterior a posição 6
print('p5: ',lista1[3:]) # a partir da posição 3 imprime todos elementos
print('p6: ',lista1[1:8:2]) # a partir da posição 1 até o elemento anterior a posição 8, imprime com intervalo de 2 em 2


for elemento in lista1:
    print('p7: ',elemento)

print('p8 Tamanho da lista: ', len(lista1))

for i in range(len(lista1)):
    print('p9: ',i, lista1[i])


