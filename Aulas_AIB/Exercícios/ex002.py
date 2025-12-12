#Exercicio 2
#Crie um programa que leia o nome do utilizador, posteriormente, apresente uma mensagem de boas-vindas. A mensagem deve incluir o nome do utilizador introduzido.

#Versão 0.1.
utilizador = str(input('Digite o seu nome de utilizador: '))
print('Bem vindo,',utilizador,'!')

#Versão 0.3.
print(f'Bem vindo, {utilizador}!')

#Versão 0.3.
print('Bem vindo, {}!'.format(utilizador))