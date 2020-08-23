n1 = float(input('Informe a sua primeira nota: '))
n2 = float(input('Informe a sua segunda nota: '))

media = (n1+n2)/2
if (media==10):
    print('Aprovado com Distição, Sua média foi {}'.format(media))
elif (media>=7):
    print('Aprovado, Sua média foi {}'.format(media))
else:
    print('Reprovado, Sua média foi {}'.format(media))