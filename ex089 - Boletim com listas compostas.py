lista = list()
while True:
    nome = str(input('Nome: ')).upper()
    nota1 = float(input(f'Nota 1: '))
    nota2 = float(input(f'Nota 2: '))
    media = (nota1+nota2) / 2
    #lista 0: nome, lista 1: notas, lista2: media
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print('-='*30)
print(f'{'No.':<6}{'NOME':<10}{'MÉDIA':>8}')
print(f'-'*26)
for i, a in enumerate (lista):
    print(f'{i:<6}{a[0]:<10}{a[2]:>8.1f}')
    #i, numera as linhas da lista
    #[0], acessa os dados da coluna 'nome'
    #[2], acessa os dados da coluna 'media'
while True:
    print('-='*30)
    opc = int(input('Mostrar nostas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista) -1:
        #[0] acessa os dados q estão na lista 0, nome
        #[1) acessa os dados q estão na lista 1, notas
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('<<< VOLTE SEMPRE >>>')