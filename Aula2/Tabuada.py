valor = int(input('Digite o valor da tabuada: '))
print('Tabuada do número: {}'.format(valor))
for i in range(11):
    res = valor*i
    print('{} x {:2} = {}'.format(valor, i, res))