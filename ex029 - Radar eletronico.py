#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

#cores adicionadas após a aula 11,

velocidade = float(input('Qual a velocidade atual do veículo? '))

if velocidade > 80:
    print('O veículo está acima da velocidade permitida!')
    print('O veículo foi multado em \033[31;40mR$ {:.2f}\033[m'.format((velocidade-80)*7.0))   #cores adicionadas e retiradas com o code \033[m
else:
    print('O veículo está dentro da velocidade permitida')
