#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Programa gerador de PA')
print('-='*11)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <=10:
    print('{} → '.format(termo),end='')
    termo += razão
    cont += 1
print('FIM')
