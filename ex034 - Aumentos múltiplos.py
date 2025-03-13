#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: R$ '))

if salario <= 1250:
    print('Com um reajuste de 15%, o salário atualizado do funcionário passa a ser R$ {:.2f}'.format((salario * 0.15)+salario))
else:
    print('Com um reajuste de 10%, o salário atualizado do funcionário passa a ser R$ {:.2f}'.format((salario * 0.10) + salario))
