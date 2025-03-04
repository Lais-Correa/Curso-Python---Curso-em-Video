#faça um programa que leia a largura e a altura de uma parede em metros.
# calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2metros quadrados

print('Seja bem vindo ao calculador de tinta \nDigite as informações solicitadas para saber a quantidade de tinta necessaria!')
largura = float(input('\nQual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

area = largura * altura

print('Conforme as informações digitadas, a área da parede é {:.2f} m2.' . format(area))

litros = area/2

print('Cada litro de tinta, pinta uma área de 2 metros quadrados. A sua parede tem {:.2f}m2, portanto, precisa de {:.2f} litros de tinta'.format(area,litros))
