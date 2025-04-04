'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

print('='*35)
print('{:^35}'.format('NUMERAIS POR EXTENSO'))
print('=' * 35)

cont =('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')

print(f'Você digitou o número {num}, e sua versão por extenso se escreve: {cont[num]}.')
