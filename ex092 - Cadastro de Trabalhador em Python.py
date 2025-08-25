#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
trabalhador = {}

trabalhador['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
trabalhador['Idade'] = datetime.now().year - nasc
trabalhador['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$ '))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + ((trabalhador['Contratação'] + 35) - datetime.now().year)

print('-='*30)
for k, v in trabalhador.items():
    print(f'  - {k} tem o valor {v}')
    