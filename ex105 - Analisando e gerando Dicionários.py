def notas(*n, sit = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'APROVADO'
        elif r['media'] >= 5:
            r['situação'] = 'EM RECUPERAÇÃO'
        else:
            r['situação'] = 'REPROVADO'
    return r


#programa principal
resp = notas(5.5, 2.5, 8.5,9,10, sit = True)
print(resp)
#help(notas)