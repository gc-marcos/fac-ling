faltas = int(input('Faltas: '))
nota1 = float(input('Digite nota 1:'))
nota2 = float(input('Digite nota 2: '))
media = (nota2 + nota1) / 2
if faltas <= 10 and media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
