#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
computador = randint (0,5) #faz o computador 'pensar'
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivihar

if jogador == computador: #finalização do jogo
    print('Parabens! você conseguiu me vencer!') #se os números são iguais
else:
    print('Você perdeu! \nEu pensei no número {} e não no {}!'. format(computador,jogador)) #se os números são diferentes
