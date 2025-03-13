#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('Analisador de triângulos')
print('-='*12)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As medidas digitadas PODEM FORMAR um triângulo')
else:
    print('As medidas digitadas NÃO PODEM FORMAR um triângulo')

