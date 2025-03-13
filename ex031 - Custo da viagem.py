#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

#cores adicionadas após a aula 11,


distancia = float(input('Qual é a distância (em KM) da sua viagem? '))

print('Você está prestes a começar uma viagem de {} Km'.format(distancia))
if distancia <= 200:
    print('O preço da sua passagem será de R$ \033[4m{:.2f}\033[m'.format(distancia * 0.50))    #cores adicionadas e retiradas com o code \033[m
else:
    print('O preço da sua passagem será de R$ \033[4m{:.2f}\033[m'.format(distancia * 0.45))
