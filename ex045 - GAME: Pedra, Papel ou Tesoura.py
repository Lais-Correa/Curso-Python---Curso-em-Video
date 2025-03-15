#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('{:=^20}'.format(' JOKENPÔ '))
print('''Suas opçoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

print('\n\033[1;32mJO\033[m',end='')
sleep(1)
print('\033[1;34mKEN\033[m',end='')
sleep(1)
print('\033[1;31mPÔ!\033[m')
sleep(1)

print('-='*15)
print('O computador escolheu: {}'. format(itens[computador]))
print('O jogador escolheu: {}'. format(itens[jogador]))
print('-='*15)

if computador == 0: #computador jogou PEDRA
    if jogador == 0: # jogador jogou PEDRA
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 1: #jogador jogou PAPEL
        print('\033[1;33mCOMPUTADOR VENCE!\033[m')
    elif jogador == 2: # jogador jogou TESOURA
        print('\033[1;33mJOGADOR VENCE!\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:  # jogador jogou PEDRA
        print('\033[1;33mCOMPUTADOR VENCE!\033[m')
    elif jogador == 1:  # jogador jogou PAPEL
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 2:  # jogador jogou TESOURA
        print('\033[1;33mJOGADOR VENCE!\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:  # jogador jogou PEDRA
        print('\033[1;33mJOGADOR VENCE!\033[m')
    elif jogador == 1:  # jogador jogou PAPEL
        print('\033[1;33mCOMPUTADOR VENCE!\033[m')
    elif jogador == 2:  # jogador jogou TESOURA
        print('\033[1;33mEMPATE\033[m')
    else:
        print('JOGADA INVÁLIDA')
