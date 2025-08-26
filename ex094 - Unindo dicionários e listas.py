#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos
# os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade
# C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

pessoa = {}
todos = []
soma = media = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO!, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    todos.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO!, digite apenas M ou F.')
    if resposta == 'N':
        break
print('=-'*20)
print(f'A) Ao todo temos {len(todos)} pessoas cadastradas')
media = soma / len(todos)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ',end='')
for p in todos:
    if p['Sexo'] in 'Ff':
        print(f'{p['Nome']} ', end='')
print()
print(f'D) Lista de pessoas que estão acima da média: ')
for p in todos:
    if p['Idade'] >= media:
        print('    ',end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print()
print('<< PROGRAMA ENCERRADO >>')




