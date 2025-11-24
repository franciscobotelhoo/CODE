import math

print('---------Calculadora de Perímetros e Áreas---------')
print('Selecione uma das opções seguintes. \n1. Triângulo; \n2. Retângulo; \n3. Círculo.')
op = int(input('Escolhe a opção: '))
area = float(0)
perimetro = float(0)

if op == 1:
    b = float(input('Indica a medida da base do triângulo: '))
    l1 = float(input('Indica a medida de outro lado do triângulo: '))
    l2 = float(input('Indica a medida de outro lado do triângulo: '))
    h = float(input('Indica a medida da altura do triângulo: '))
    area = (b*h)/2
    perimetro = b+l1+l2
    print(f'O perímetro do triângulo é {perimetro} e a área é {area}')
elif op == 2:
    lh = float(input('Indica a medida de um lado horizontal do retângulo: '))
    lv = float(input('Indica a medida de um lado vertical do retângulo: '))
    perimetro = (lh * 2 ) + (lv * 2)
    area = lh * lv
    print(f'O perímetro do retângulo é {perimetro} e a área é {area}')
elif op == 3:
    raio = float(input('Indica a medida do raio do círculo: '))
    perimetro = 2 * math.pi * raio
    area = math.pi * raio**2
    print(f'O perímetro do círculo é {perimetro:.4f} e a área é {area:.4f}')