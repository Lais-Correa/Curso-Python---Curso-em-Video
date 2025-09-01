from time import sleep

def contador(i, f, p):

    if p < 0:
        p *= -1

    elif p == 0:
        p = 1

    print('-='*20)
    print(f'Contagem de {i} até o {f} de {p} em {p}')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
            sleep(0.3)
        print('>>> FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
            sleep(0.3)
        print('>>> FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
con = int(input('Passo:  '))
contador(ini, fim, con)