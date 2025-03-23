
while True:
    num = int(input('Digite um número para ver a tabuada: '))
    if num < 0:
        break
    print('-' * 20)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-' * 20)
print('PROGRAMA DE TABUADA ENCERRADO! Volte sempre')
