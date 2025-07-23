lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input(f'Nota 1: '))
    nota2 = float(input(f'Nota 2: '))
    media = (nota1+nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print('-='*30)
print(f'{'No.':<6}{'NOME':<6}{'MÉDIA':>6}')
print(f'-'*26)
for i, a in enumerate (lista):
    print(f'{i}{}')
print(lista)
