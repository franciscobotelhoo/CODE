import random
pc = random.randint(1,3)
print('1 - Pedra\n2 - Papel\n3 - Tesoura')
user = int(input('Qual é a sua jogada: '))
if pc == 1 and user == 3:
    print('O computador escolheu pedra. Você perdeu!')
elif pc == 2 and user == 1:
    print('O computador escolheu papel. Você perdeu!')
elif pc == 3 and user == 2:
    print('O computador escolheu tesoura. Você perdeu!')
elif pc == 1 and user == 2:
    print('Parabéns, você ganhou!')
elif pc == 2 and user == 3:
    print('Parabéns, você ganhou!')
elif pc == 3 and user == 1:
    print('Parabéns, você ganhou!')
elif pc == 1 and user == 1:
    print('Empate!')
elif pc == 2 and user == 2:
    print('Empate!')
elif pc == 3 and user == 3:
    print('Empate!')
else:
    print('Opção inválida!')