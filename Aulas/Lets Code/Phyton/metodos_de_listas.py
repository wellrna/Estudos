
# Metodos de Listas

lista = [1, 3, 12, 8, 2]

# append

print("Antes do append", lista)

lista.append(3) # adiciona o 3 ao final da lista

print('Depois do append', lista)


# insert

lista.insert(2, 10) # insere o valor na posição informada. no exemplo adiociona ma posição 2 o valor 10

print('Depois do insert', lista)


# extend

lista2 =[1, 2, 3]

lista.extend(lista2)

print('Depois do extend', lista)


# pop

lista.pop() # elimina o ultimo valor da lista

print('Depois do pop sem indice', lista)

lista.pop(0) # elimina o valor da posição 0

print('Depois do pop sem indice', lista)


# remove

lista.remove(3) # remove o primeiro elemento que possuir o valor 3 na lista

print('Depois do pop remove', lista)


# count

print('Informa a quantidade de 2 na lista', lista.count(2))

# index

print('Informa o indice de um determinado valor, exemplo 12: ', lista.index(12))

# sort

lista.sort() # ordena em ordem crescente

print('sort',lista)

lista.sort(reverse=True) # ordena em ordem decrescente

print('sort-reverse',lista)


# Funções

# len

print(len(lista)) # Informa a quantidade elementos da lista

# sum

print(sum(lista)) # Informa a soma dos elementos da lista

# max

print(max(lista)) # Informa o maior dos elementos da lista

# min

print(min(lista)) # Informa o menor dos elementos da lista
