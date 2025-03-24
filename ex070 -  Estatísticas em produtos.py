#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

total = totmil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Nome do produto: ')).strip() .upper()
    preço = float(input('Preço: R$'))
    cont += 1

    total += preço        #faz o total da compra

    if preço >= 1000:         #verifica os produtos q custam mais de mil reais
        totmil += 1

    if cont == 1 or preço < menor:              #verifica o produto mais barato
        menor = preço
        barato = nome

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi "{barato}" que custa R${menor:.2f} ')
