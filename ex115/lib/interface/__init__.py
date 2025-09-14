def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário enterrompeu o programa.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    print('-' * tam)


def cabeçalho(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[34m{c}\033[m - \033[m{item}\033[m')
        c+=1
    linha()
    opc = LeiaInt('Sua Opção: ')
    return opc