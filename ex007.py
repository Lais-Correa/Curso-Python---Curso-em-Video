#Desenvolva um programa que leia os duas notas  de um aluno, calcule e mostre a media


n1=float(input('Digite a primeira nota do aluno:'))
n2=float(input('Digite a segunda nota do aluno:'))
media= (n1+n2)/2
print('As notas digitadas foram: {} e {}, e a media entre elas é: {}'.format(n1,n2,media))