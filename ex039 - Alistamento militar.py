#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('Digite o ano de nascimento: '))
sexo = input('Digite seu sexo: (Opções aceitas: MASCULINO ou FEMININO) ') .strip().upper()

ano_atual = date.today().year
idade = ano_atual - nasc

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, ano_atual))

if sexo == 'MASCULINO':
    if idade < 18:
        print('Ainda faltam {} anos para o alistamento'.format(18-idade))
        print('Você deve se alistar em {}'.format(nasc+18))
    elif idade == 18:
        print('Você deve se alistar IMEDIATAMENTE!')
    elif idade > 18:
        print('Você ja deveria ter se alistado há {} anos'.format(idade-18))
        print('Seu alistamento foi em {}'.format(nasc+18))

elif sexo == 'FEMININO':
    print('O alistamento militar FEMININO não é obrigatório.')
    opcao = input('Você deseja se alistar voluntáriamente? (S/N)').strip().upper()

    if opcao == 'S' and 18 <= idade <= 48:
        print('Você pode ir à junta militar mais próxima para se alistar voluntariamente')
    else:
        print('Você não precisa se alistar.')

else:
    print('Opção inválida')
    