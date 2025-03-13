# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

#cores adicionadas após a aula 11

from random import choice

aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice (lista)

print('O aluno escolhido foi \033[4;36m{}\033[m'. format(escolhido)) #cores adicionadas e retiradas com o code \033[m