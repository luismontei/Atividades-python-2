print('Auto Posto Monteiro')
print('Preço do álcool: 1.90\nAté 20 litros, 3% de desconto por litro\nAcima de 20 litros, 5% de desconto')
print('Preço da gasolina: 2.50\nAté 20 litros, 4% de desconto por litro\nAcima de 20 litros, 6% de desconto')
combustivel = input('Informe o tipo de combustível se for gasolina G e se for álcool A: ')
litros = float(input('Informe quantos litros de combustível que queira abastecer: '))
if (combustivel=='A') and (litros<=20):
        alcool=(litros*1.90)
        desconto1= alcool-(alcool*3/100)
        print('Total a pagar foi {}'.format(desconto1))
elif (combustivel=='A') and (litros>20):
        alcool=(litros*1.90)
        desconto2=alcool-(alcool*5/100)
        print('Total a pagar foi {}'.format(desconto2))
if (combustivel=='G') and (litros<=20):
    gasolina=(litros*2.50)
    desconto3= gasolina-(gasolina*4/100)
    print('Total a pagar foi {}'.format(desconto3))
elif(combustivel=='G') and (litros>20):
    gasolina=(litros*2.50)
    desconto4=(gasolina-(gasolina*4/100))
    print('Total a pagar foi {}'.format(desconto4))
