#faça um algorítimo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto

#corea adicionada após a aula 11

preco_atual = float(input('Qual o preço atual do produto? R$'))

novo_preco = preco_atual - (preco_atual*0.05)
print('O produto que custava \033[31mR${:.2f}\033[m, com  a promoção de 5% de desconto, o valor passa a ser de \033[32mR${:.2f}\033[m'. format(preco_atual, novo_preco))#cores adicionadas e retiradas com o code \033[m