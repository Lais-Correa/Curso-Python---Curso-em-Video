#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#cores adicionadas após a aula 11,

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi \033[4;32m{}\033[m'.format(menor))
print('O maior valor digitado foi \033[4;31m{}\033[m'.format(maior))#cores adicionadas e retiradas com o code \033[m


