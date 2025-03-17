#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range (1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?  '.format(pess)))
    idade = ano_atual - nasc
    if idade <= 21:
        totmaior += 1
    else:
        totmenor += 1

print('Ao todo, tivemos \033[34m{}\033[m pessoas \033[34mMAIORES DE IDADE\033[m.'.format(totmaior))
print('E tambem tivemos \033[35m{}\033[m pessoas \033[35mMENORES DE IDADE\033[m.'.format(totmenor))
