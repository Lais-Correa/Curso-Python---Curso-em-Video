#Faça um algorítimo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento

salario_atual = float(input('Informe o salário atual do funcionário: R$'))

salario_com_aumento = salario_atual + (salario_atual*0.15)

print('Com aumento de 15%, o salário atualizado do funcionário passa a ser R$ {:.2f}' .format(salario_com_aumento))