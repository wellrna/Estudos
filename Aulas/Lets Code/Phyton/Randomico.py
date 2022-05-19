import random # necessário para inicializar o módulo random

lista = [1, 3, 12, 8, 2, 1, 2, 3, 10, 50, 30, 40, 25, 60, 5]

random.seed(8)
print(random.random()) # resultado: 0.2267058593810488
print(random.random()) # resultado: 0.9622950358343828
 
random.seed(8)
print(random.random()) # resultado: 0.2267058593810488
print(random.random()) # resultado: 0.9622950358343828
 
random.seed(8)
numeros = random.getstate()
print(random.sample(range(10), k=5))
#resultado: [3, 5, 6, 1, 7]

random.seed(10)
print(random.sample(range(10), k=5))
#resultado : [9, 0, 6, 3, 4]

random.setstate(numeros)
print(random.sample(range(10), k=5))
#resultado: [3, 5, 6, 1, 7]

print(random.randrange(1, 100, 1))

print(random.randrange(10, 100, 5))
#resultado: 85

print(random.randrange(10, 100, 5))
#resultado: 20

print(random.randrange(10, 100, 5))
#resultado: 60

print(random.randint(1,100))

print(random.randint(2, 10))
#resultado: 7

print(random.randint(2, 10))
#resultado: 2

print(random.randint(2, 10))
#resultado: 10

print(random.randint(2, 10))
#resultado: 7

lista_nomes=['Maria', 'João', 'Pedro', 'Cláudia']
print(random.choice(lista_nomes))
#resultado: Maria

nome = 'Ivani'
print(random.choice(nome))
#resultado: v

tupla_nomes=('Maria', 'João', 'Pedro', 'Cláudia')
print(random.choice(tupla_nomes))
#resultado: Cláudia

lista_dicionario_nomes= [{"nome": "Maria", "idade": 20}, {"nome": "Cláudia", "idade": 25}]
print(random.choice(lista_dicionario_nomes))
#resultado: {'nome': 'Maria', 'idade': 20}

print(random.choice(range(2,20)))
#resultado: 16

print(random.choice(range(2,20)))


print('choice range 0',random.choice(range(1,100)))
print('choice range 1',random.choice(range(1,100)))
print('choice range 2',random.choice(range(1,100)))
print('choice range 3',random.choice(range(1,100)))
print('choice range 4',random.choice(range(1,100)))
print('choice range 5',random.choice(range(1,100)))
print('choice range 6',random.choice(range(1,100)))
print('choice range 7',random.choice(range(1,100)))
print('choice range 8',random.choice(range(1,100)))
print('choice range 9',random.choice(range(1,100)))


random.seed()          # utilizou o horário do sistema como base
print('random 0',random.random())
print('random 1',random.random())
print('random 2',random.random())
print('random 3',random.random())
print('random 4',random.random())
print('random 5',random.random())
print('random 6',random.random())
print('random 7',random.random())
print('random 8',random.random())
print('random 9',random.random())

lista_choice=[]
lista_random=[]
lista_random3=[]
contador = 0
var_choice =0.01234567890123456789
var_random =0.01234567890123456789
print(var_choice, type(var_choice))
print(var_random, type(var_random))
while contador <= 100:
    var_choice = random.choice(range(1,100))
    lista_choice.append(var_choice)
    var_random = random.random()
    lista_random.append(var_random)
    lista_random3.append(int(var_random*100))
    contador = contador + 1

print(lista_choice)
lista_choice2 = lista_choice
lista_choice2.sort()
print(lista_choice2)
print(lista_random)
lista_random2 = lista_random
lista_random2.sort()
print(lista_random2)
print(lista_random3)
lista_random4 = lista_random3
lista_random3.sort()
print(lista_random4)
