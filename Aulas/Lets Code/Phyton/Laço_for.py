# Laço de repetição for

for i in range(10): # conta de zero a 9 sempre para antes do numero final
    print(i)

for i in range(1,11): #conta de 1 a 10 sempre para antes do numero final
    print(i)

for i in range(1,13,3): #conta de 1 a 10 sempre para antes do numero final. O terceito numero é o incremento na contagem
    print(i)


soma = 0
for i in range(1, 4):
    nota = float(input(f"Informe a sua nota {i}:"))
    soma = soma + nota

print(soma)