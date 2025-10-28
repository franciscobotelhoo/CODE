mediaidade = 0
somaidade = 0
idadehomemvelho = 0 
nomehomemvelho = ''
mulheresmenos20 = 0

for c in range (1, 5):
    print('----{}º Participante----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M\F]:')).upper()

    somaidade += idade

    if sexo == 'M' and idade>idadehomemvelho:
        idadehomemvelho = idade
        nomehomemvelho = nome
    if sexo == 'F' and idade<20:
        mulheresmenos20 +=1

mediaidade = somaidade/4

print('\nA média de idade do grupo é de {} anos.'.format(mediaidade))
print('O nome do homem mais velho do grupo é {}.'.format(nomehomemvelho))
print('No total existem {} mulheres com menos de 20 anos.'.format(mulheresmenos20))