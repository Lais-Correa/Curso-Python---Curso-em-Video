#crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
#considere a cotação de US$1 = R$ 3,27

reais = float(input('Quantos Reais você tem na carteira?: '))
dolares = reais / 3.27
print('Considerando que a cotação do Dólar está R$ 3,27, você pode comprar US$ {:.2f}.' .format(dolares) )
