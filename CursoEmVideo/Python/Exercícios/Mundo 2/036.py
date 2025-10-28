vcasa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o salário do comprador? '))
anos = float(input('Em quantos anos você quer pagar? '))
if vcasa <= 0 or salario <= 0 or anos <= 0:
    print('Valores inválidos! Digite valores positivos.')
    exit()
prestacao = vcasa/(anos*12)
if prestacao>=(salario*0.30):
    print('Você não irá poder comprar a casa.')
else:
    print('Financiamento aprovado! A prestação será de R${:.2f} por mês.'.format(prestacao))