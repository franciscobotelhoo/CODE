pesomaior = 0
pesomenor = 1000000000
for c in range(0,5):
    p = float(input('Digite o peso: '))
    if p>pesomaior:
        pesomaior=p
    if p<pesomenor:
        pesomenor=p
print(pesomaior)
print(pesomenor)