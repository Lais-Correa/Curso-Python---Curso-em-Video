'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''


lista = []

for c in range (5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print('Número adicionado no final da lista.')
    elif n > lista[len(lista)-1]:
        lista.append(n)
        print('Número adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista [pos]:
                lista.insert(pos,n)
                print(f'Número adicionado na posição {pos} da lista.')
                break
            pos += 1
print('-='*27)
print(f'Os valores digitados em ordem foram {lista}')