'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

#sorteia os números
from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10),
     randint(1,10), randint(1,10))

#obtem os maiores números
maior = max(numeros)
menor = min(numeros)

#exibe os números, destacando o maior e menor:
print('Os valores sorteados foram: ', end='')
for n in numeros:
    if n == maior:
        print(f'\033[31m{maior} \033[m', end='')
    elif n == menor:
        print(f'\033[32m{menor} \033[m', end='')
    else:
        print(f'{n} ', end='')

#exibe o maior e menor
print(f'\n- O maior valor sorteado foi \033[31m{maior}\033[m.')
print(f'- O menor valor sorteado foi \033[32m{menor}\033[m.')
