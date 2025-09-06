def aumentar(preço = 0, taxa = 0, formato = False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: O preço que se quer reajustar
    :param taxa: qual a taxa de aumento
    :param formato: que saida formatada ou não?
    :return: o valor reajustado com ou sem formatação
    """
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço = 0, taxa = 0, formato = False):
    """
        -> Calcula a diminuição de um determinado preço,
        retornando o resultado com ou sem formatação.
        :param preço: O preço que se quer reajustar
        :param taxa: qual a taxa de diminuição
        :param formato: que saida formatada ou não?
        :return: o valor reajustado com ou sem formatação
        """
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço = 0, formato = False):
    """
    -> Calcula o dobro de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: O preço que se quer reajustar
    :param formato: que saida formatada ou não?
    :return: o valor reajustado com ou sem formatação
    """
    res = preço * 2
    return res if formato is False else moeda(res)

def metade(preço = 0, formato = False):
    """
    -> Calcula a metade de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: O preço que se quer reajustar
    :param formato: que saida formatada ou não?
    :return: o valor reajustado com ou sem formatação
    """
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço = 0, moeda = 'R$ '):
    """
    -> Corrige o valor para ficar vizualmente mais bonito,
    retornando o resultado com ou sem formatação.
    :param preço: O preço que se quer reajustar
    :param moeda: simbolo de dinheiro
    :return: o valor reajustado com ou sem formatação
    """
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço = 0, taxaa = 10, taxar = 5):
    """
    -> exibe os valores calculados,
    retornando o resultado com ou sem formatação.
    :param preço: O valor que quer reajustar
    :param taxaa: taxa de aumento
    :param taxar: taxa de redução
    :return: o valor reajustado com ou sem formatação
    """
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print('-' * 30)
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço:\t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço,taxaa,True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preço,taxar,True)}')
    print('-' * 30)