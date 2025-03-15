#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto, à vista no cartão: 5% de desconto, em até 2x no cartão: preço formal, 3x ou mais no cartão: 20% de juros.

print('{:=^40}'.format(' LOJAS GUANBARA '))
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão''')
opção = int(input('Qual a forma de pagamento? '))

if opção == 1:
    print('A forma de pagamento escolhida foi: \033[34mà vista dinheiro/cheque\033[m, tem 10% de desconto!')
    print('Valor a pagar é de R$ {:.2f}'. format(preco-(preco*0.10)))
elif opção == 2:
    print('A forma de pagamento escolhida foi: \033[34mà vista no cartão\033[m, tem 5% de desconto!')
    print('Valor a pagar é de R$ {:.2f}'.format(preco - (preco * 0.05)))
elif opção == 3:
    print('A forma de pagamento escolhida foi: \033[34m2x no cartão\033[m')
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(preco/2))
    print('Valor a pagar é de R$ {:.2f}'.format(preco))
elif opção == 4:
    parcelas = int(input('Quantas parcelas?'))
    preco1 = (preco + (preco * 0.20)) / parcelas
    print('A forma de pagamento escolhida foi: \033[34m{}x no cartão\033[m,esta forma de pagamento adiciona 20% de juros'.format(parcelas))
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(parcelas, preco1))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,preco1*parcelas))
else:
    print('Opção errada')
    