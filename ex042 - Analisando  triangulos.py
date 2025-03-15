#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais, ISÓSCELES: dois lados iguais, um diferente, ESCALENO: todos os lados diferentes

print('Analisador de triângulos')
print('-='*12)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As medidas digitadas \033[4mPODEM FORMAR\033[m um triângulo', end='')    #cores adicionadas e retiradas com o code \033[m
    if r1 == r2 == r3:
        print('\033[34m EQUILATERO\033[m!')
    elif r1 != r2 != r3 != r1:
        print('\033[34m ESCALENO \033[m!')
    else:
        print('\033[34m ISÓSCELES \033[m!')
else:
    print('As medidas digitadas \033[31m NÃO PODEM FORMAR \033[m um triângulo')    #cores adicionadas e retiradas com o code \033[m
