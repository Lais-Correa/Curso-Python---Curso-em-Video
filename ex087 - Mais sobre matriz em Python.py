matriz = [ [0, 0,0], [0, 0, 0], [0, 0, 0] ]
spares = mai = scoluna = 0
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range (0,3):
    for c in range(0,3):
        print(f'[{matriz [l][c]:^5}] ',end='')
        if matriz [l] [c] % 2 == 0:        #verifica os valores pares da matriz
            spares += matriz [l] [c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spares}.')
for l in range(0, 3):                       #verifica os valores da terceira coluna
    scoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scoluna}.')
for c in range(0, 3):                       #descobre qual é o maior valor da 2˚linha
    if c == 0:
        mai = matriz [1][c]
    elif matriz [1][c] > mai:
        mai = matriz [1][c]
print(f'O maior elementos da segunda linha é {mai}.')