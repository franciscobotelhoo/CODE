import random

alunos = ['Jorge', 'Manuel', 'Tomás', 'Rodrigo']
random.shuffle(alunos)
print('A lista é: {}'.format(', '.join(alunos)))