'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('aprender', 'programar', 'linguagem', 'python','curso','gratis','estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ',end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')
print('\n')
print('-'*30)
print('Analise de vogais finalizado!')