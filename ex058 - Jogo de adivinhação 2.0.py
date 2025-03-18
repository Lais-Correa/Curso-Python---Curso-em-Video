# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint (0,10) #faz o computador 'pensar'
print('-=-' *20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' *20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivihar
    palpites += 1
    if jogador == computador:
        acertou = True
    else: # se o jogador n acertou, o computador da uma dica de número maior ou menor
        if jogador < computador:
            print('O número é \033[36mMAIOR\033[m, tente mais uma vez.')
        elif jogador > computador:
            print('O número é \033[31mMENOR\033[m, tente mais uma vez.')
print('\033[32mParabens!\033[m você conseguiu me vencer com {} tentativas!'.format(palpites))