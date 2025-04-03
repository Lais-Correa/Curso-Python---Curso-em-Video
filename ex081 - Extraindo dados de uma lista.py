'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''


num = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar...')
    r = str(input('Quer continuar? [S/N] ')).upper()
    if r in 'N':
        break
print('-='*20)
print(f'Você digitou {len(num)} elementos. ')
num.reverse()
print(f'A lista de valores em ordem decrescente foi {num}')
if 5 in num:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não foi digitado')
    