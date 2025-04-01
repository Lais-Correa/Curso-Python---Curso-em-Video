'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''

num = []

for n in range(0,5):
    num.append(int(input(f'Digite um número na posição {n}: ')))

maior = max(num)
menor = min(num)

print('-='*20)
print(f'Você digitou os valores: {num}')
print(f'O maior número digitado foi {maior}, nas posições ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor número digitado foi {menor}, nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
        