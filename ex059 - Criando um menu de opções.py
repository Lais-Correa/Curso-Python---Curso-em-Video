#Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar, [ 2 ] multiplicar
#[ 3 ] maior ,[ 4 ] novos números, [ 5 ] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''Opções:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('O resultado de {} + {} é {}'.format(n1,n2,soma))
    elif opcao == 2:
        mult = (n1 * n2)
        print('O resultado de {} * {} é {}'.format(n1,n2,mult))
    elif opcao == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}'.format(n1,n2))
        else:
            print('O número {} é maior que o número {}'.format(n2, n1))
    elif opcao == 4:
        print('Digite os novos valores:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('-=' * 10)
    sleep(2)
print('Programa encerrado!')
