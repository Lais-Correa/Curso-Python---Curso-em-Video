#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.No final,
# mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas
# c) Uma listagem com as pessoas mais leves.

pessoas = list()
dado = list()
maiorpeso = menorpeso = totpess = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dado[1]
    else:
        if dado[1] > maiorpeso:
            maiorpeso = dado[1]
        if dado[1] < menorpeso:
            menorpeso = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    totpess += 1
    resp = str(input('Quer continuar? [S/N]')).upper().strip()
    if resp == 'N':
        break


print('-='*30)
print(f'Ao todo, você cadastrou {totpess} pessoas.') #ou usar o len(pessoas)
print(f'O maior peso foi de {maiorpeso} KG. Peso de ',end= '')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorpeso} KG. Peso de ',end= '')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}] ', end='')
print()
