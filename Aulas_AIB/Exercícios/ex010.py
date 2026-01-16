#Exercício 010
#Crie um programa que lê a quantidade de dinheiro que tem na carteira. Apresente na consola a conversão desse valor em dólares. Apresente também a conversão desse valor em libras inglesas.

print('========================================\n Conversor de Euros para dólar e libra\n========================================')

dinheiro = float(input('\nIndique o valor que tem na carteira em €, não inclua o símbolo: '))

print(f'\nO valor que tem na carteira - {dinheiro:.2f}€ corresponde a:\n{dinheiro*1.16:.2f}$\n{dinheiro*0.87:.2f}£')
