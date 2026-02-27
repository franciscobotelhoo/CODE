from random import choice

n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))

e = choice([n1, n2, n3, n4])
print(f'O aluno escolhido foi {e}')
