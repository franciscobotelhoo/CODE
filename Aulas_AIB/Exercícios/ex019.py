#Crie um programa que preenche uma lista com nomes de alunos, retorne um nome aleatoriamente a partir da lista.

from random import choice
print('EXERCÍCIO 019 - Escolher um nome da lista')
a1 = input("\nIntroduza o nome do aluno 1: ")
a2 = input("\nIntroduza o nome do aluno 2: ")    
a3 = input("\nIntroduza o nome do aluno 3: ")
a4 = input("\nIntroduza o nome do aluno 4: ")
lista_alunos = [a1, a2, a3, a4]
aluno_escolhido = choice(lista_alunos)
print(f"\nO(A) aluno(a) escolhido(a) aleatoriamente foi {aluno_escolhido}.")