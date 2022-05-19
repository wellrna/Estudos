# Estruturas Condicionais

idade = 20

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')


media = float(input('Informe a media do aluno: '))

if media >= 7:
    print('Você foi aprovado!')
elif media >= 5:
    print('Recuperação!')
else:
    print('Você foi reprovado!')


# media = 10
media = float(input('Informe a media do aluno: '))
presenca = int(input('Informe o % de presença do aluno: '))

if media >= 7 and presenca >= 70:
    print('Aprovado!!')
    print('Parabéns!!')
else:
    print('Reprovado!')
    print('Tente novamente!')