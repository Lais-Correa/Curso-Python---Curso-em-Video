from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVA PESSOA', 'SAIR DO SISTEMA'])
    if resposta == 1:
        #opção de listar o conteudo do arquivo
        lerArquivo(arquivo)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = LeiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabeçalho('SAINDO DO SISTEMA...Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

