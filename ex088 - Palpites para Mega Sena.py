from random import randint
from time import sleep, process_time_ns

lista = list()
jogos = list()
print('=-'*30)
print(f'{'SIMULADOR DE MEGA SENA':^60}')
print('=-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <=quant:
    cont = 0
    while True:
        num = randint (0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
sleep(0.)
print(f'{'          Sorteando os números em...'}',end='')
print('3...',end='')
sleep(0.5)
print('2...',end='')
sleep(0.5)
print('1...','           ')
print('=-'*30)
for i, l in enumerate(jogos):
    print(f'{i+1}ª Jogo {l}')
    sleep(0.5)
print('=-' * 30)
print(f'{'BOA SORTE!':^60}')
print('=-'*30)