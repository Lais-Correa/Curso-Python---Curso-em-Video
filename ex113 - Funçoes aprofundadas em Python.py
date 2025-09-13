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

def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário enterrompeu o programa.\033[m')
            return 0
        else:
            return n

num1 = LeiaInt('Digite um valor Inteiro: ')
num2 = LeiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2}')