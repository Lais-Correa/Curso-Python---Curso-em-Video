#faça um algorítimo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto

preco_atual = float(input('Qual o preço atual do produto? R$'))

novo_preco = preco_atual - (preco_atual*0.05)
print('O produto que custava R${:.2f}, com  a promoção de 5% de desconto, o valor passa a ser de R${:.2f}'. format(preco_atual, novo_preco))