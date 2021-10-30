valor = float(input('Digite quantos reais voce tem: R$'))
res = valor/5.64    # 5.64 valor do dolar
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(valor, res))