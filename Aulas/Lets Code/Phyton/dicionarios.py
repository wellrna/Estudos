# DICIONARIOS

# Criando dicionários

dicionario = {}
dicionario1 = dict()

dicionario2 = {'nome': 'Wellington', 'idade': 52, 'altura': 1.85 }

print(dicionario2)
print(dicionario2['idade'])

# Adicionando elementos em um dicionario

dicionario2['programador'] = True

print(dicionario2)

dicionario2['programador'] = False # Quando vc aplica este comando a uma chave existente ele sobrescreve o valor

print(dicionario2)

# iterando sobre um dicionário

for variavel in dicionario2:
    print(variavel) # nesta estrutura ele percorre o dicionario e informa as chaves do dicionário

for variavel in dicionario2:
    print(variavel, dicionario2[variavel]) # nesta estrutura ele percorre o dicionario e informa as chaves e o valor de cada chave do dicionário

# testeando se já existe uma chave no dicionário

print('peso' in dicionario2) # irá retornar false pq não existe

print('altura' in dicionario2) # irá retornar true pq existe a chave