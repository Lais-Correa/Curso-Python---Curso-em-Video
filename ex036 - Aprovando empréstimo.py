#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? R$'))

prestacao = casa / (anos * 12)
min_prestacao = (salario * 30) /100

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'. format(casa, anos, prestacao))

if prestacao <= min_prestacao:
    print('Emprestimo \33[32mCONCEDIDO\033[m! ')
else:
    print('Empréstimo \033[31mNEGADO\033[m!')