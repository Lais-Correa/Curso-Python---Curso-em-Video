#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
from os.path import split

cidade = str(input('Digite o nome da sua cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')