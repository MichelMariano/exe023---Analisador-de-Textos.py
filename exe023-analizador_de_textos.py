# Crie um programa que leia o nome completo de uma pessoa e mostre:

# Nome com todas as letras maiúsculas
# Nome com todas as letras minúsculas
# Todas as letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome... ')
print('Seu em nome em Maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {} '.format(nome.lower()))
print('Ao todo seu nome tem {} letras '.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))
