#Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('\nSistema de aluguel de carros. \nInforme as informações necessarias para os cálculos:')
print('-----------------------------------------------------')
km = float(input('Informe os Km precorridos: '))
dias = int(input('Por quantos dias o carro foi alugado: '))

rs_km = (km * 0.15)
rs_dias = dias * 60
total = rs_km + rs_dias

print('\nO total a pagar é de: {:.2f}'. format(total))
print('-----------------------------------------------------')
print('Segue abaixo a descrição dos valores: ')
print('KM - {:.2f} X R$ 0,15 por KM rodado = R${:.2f}' .format(km, rs_km))
print('DIAS - {:.0f} X R$60,00 por dias alugados = R${:.2f}' .format(km, rs_dias))