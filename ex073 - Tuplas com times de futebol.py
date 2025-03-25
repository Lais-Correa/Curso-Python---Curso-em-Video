'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

cla = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional", "São Paulo",
       "Corinthians", "Bahia", "Cruzeiro", "Vasco", "Vitória", "Atlético-MG", "Fluminense",
       "Grêmio", "Juventude", "Bragantino", "Athletico-PR", "Criciúma", "Atlético-GO", "Cuiabá" )

print('-='*15)
print('{:^30}'.format('BRASILEIRÃO 2024'))
print('-='*15)
print(f'- Lista de times do Brasileirão em 2024: {cla}')
print(f'- Os 5 primeiros são: {cla[0:5]}')
print(f'- Os 4 últimos são: {cla[-4:]}')
print(f'- Os times em ondem alfabética: {sorted(cla)}')
if 'Chapecoense' in cla:
    print(f'- O Chapecoense está na {cla.index("Chapecoense")+1}˚posiçãp')
else:
    print('- Infelizmente, o time Chapecoense não se classificou no Brasileirão.')
    