'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).upper()
    if r in 'N':
        break