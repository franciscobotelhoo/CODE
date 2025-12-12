frase = str(input('Digite uma frase:')).strip().lower().replace(' ','')
fraser = frase[::-1]
if frase == fraser:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
