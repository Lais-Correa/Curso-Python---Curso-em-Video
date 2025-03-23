from random import randint

vitorias = 0

print('-='*12)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*12)

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = (jogador + computador)
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P/I] ')) .strip().upper()[0]
    print('-'*62)
    print(f'Você jogou \033[31m{jogador}\033[m e o computador jogou \033[31m{computador}\033[m. O total é {total} e ',end='')
    print('\033[4mDEU PAR\033[m.' if total % 2 == 0 else '\033[4mDEU IMPAR\033[m.')
    print('-' * 62)
    if escolha == 'P':
        if total % 2 == 0:
            print('\033[32mVocê Venceu!\033[m')
            vitorias += 1
        else:
            print('\033[31mVocê Perdeu\033[m')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('\033[32mVocê Venceu!\033[m')
            vitorias += 1
        else:
            print('\033[31mVocê Perdeu\033[m')
            break
    print('Vamos jogar novamente...')
    print('-=' * 12)
print('-='*12)
print(f'GAME OVER! \033[34mVocê venceu {vitorias} vezes\033[m.')
