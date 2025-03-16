#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for n in range (1,7):
    num = int(input('Digite o {}ª valor: '.format(n)))
    if num  % 2 == 0:
        soma = soma+num
        cont = cont+1
print('Você me informou {} números PARES e a soma dos números é igual a {}.'. format(cont, soma))