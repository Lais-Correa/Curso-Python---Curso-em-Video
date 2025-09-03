def fatorial(num, show=False):
    """
    Calcula o fatorial de um número
    :param num: número a ser calculado 
    :param show: mostra (ou não) o calculo
    :return: o valor fatorial de um número
    """
    f =1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f*=c
    return f

#programa principal
print(fatorial(5,True))
#vai mostrar a docstring
help(fatorial)