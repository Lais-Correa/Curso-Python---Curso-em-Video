#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        tot18 += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo =str(input('Sexo: [M/F] ')).strip().upper()
    if sexo == 'M':
        totH += 1
    elif sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-='*20)
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'No total foram cadastrados {totH} homens.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')
