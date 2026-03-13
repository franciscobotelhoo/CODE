#Exercício 031
#Custo da viagem de autocarro
#Perguntar ao utiizador a distância da viagem em km
#Se a viagem for inferior a 20km, o preço é de 1.50€ por km
#Se não o custo será 1.20€ por km
#Apresente o valor total da viagem

distancia = float(input('Qual é a distância da viagem em km? '))
if distancia < 20:
    custo = distancia * 1.50
else:
    custo = distancia * 1.20   
print(f'O custo total da viagem é de {custo:.2f}€')