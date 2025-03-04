a = input('Digite algo:')
print('o tipo primitivo desse valor é ', type(a))
print('só tem espaços? ', a.isspace())
print('é um numero? ', a.isnumeric())
print('é alfabetico?', a.isalpha())
print('é alfanumerico?',a.isalnum())
print('está em maiuscula?',a.isupper())
print('está em minusculo?', a.islower())
print('está capitalizada?', a.istitle()) #quando tem a primeira letra maiuscula