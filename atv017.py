p1 = float(input('Informe o preço: '))
p2 = float(input('Informe o preço: '))
p3 = float(input('Informe o preço: '))

if (p1<p2) and (p1<p3):
    print('O preço menor é {}'.format(p1))
elif (p2<p1) and (p2<p3):
    print('O menor preço é {}'.format(p2))
else:
    print('O menor preço é {}'.format(p3))
