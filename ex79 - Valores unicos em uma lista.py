'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

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
num.sort()
print(f'Você digitou os números {num}')
