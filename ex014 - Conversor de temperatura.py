#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe a temperatura ªC: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}ªC, corresponde a {}ªF'. format(c,f))
