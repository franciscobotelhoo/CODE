salario = float(input('Qual é o seu salário? '))
if salario>=1250:
    print('Você receberá um aumento de 10%, e irá ficar com um salário de {}R$'.format(salario+(salario*0.10)))
else:
    print('Você receberá um aumento de 15%, e irá ficar com um salário de {}R$'.format(salario+(salario*0.15)))