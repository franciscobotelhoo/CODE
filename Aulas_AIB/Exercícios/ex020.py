#Crie um programa com uma lista predefinida com o nome de seis pilotos, apresente a ordem aleatória de saída dos pilotos.

from random import shuffle

print('EXERCÍCIO 020 - Sortear a ordem de saída dos pilotos')
pilotos = ['Lewis Hamilton', 'Max Verstappen', 'Valtteri Bottas', 'Sergio Perez', 'Lando Norris', 'Charles Leclerc']
shuffle(pilotos)
print(f"\nA ordem aleatória de saída dos pilotos é: {pilotos}")