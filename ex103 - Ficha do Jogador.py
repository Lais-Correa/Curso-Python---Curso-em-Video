def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


#programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
#processamento de dados, conversão de str para int e g para gol na função
if g.isnumeric():
    g = int(g)
else:
    g = 0
#está passando os dados para a função
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)