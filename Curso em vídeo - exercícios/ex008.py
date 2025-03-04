#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metros=float(input('Digite uma medida:'))
conversao1=metros*100
conversao2=metros*1000
print('Calculadora de conversões:')
print('Tranformando de metros para centímetros: {:.0f}m corresponde a {:.0f} cm.' .format(metros,conversao1))
print('Tranformando de metros para milimetros: {:.0f}m corresponde a  {:.0f} cm.' .format(metros,conversao2))