altura = 1
numPessoas = 0
while altura != 0:
    altura = float(input('Qual é a altura da pessoa? '))
    
    if altura == 0:
        break
    
    numPessoas += 1
    
    sexo = input('Qual é o sexo da pessoa? (M/F): ')
    sexo = sexo.upper()
    
    if(sexo == 'M'):
        resp = (72.7*altura) - 58
    else:
        resp = (62.1*altura) - 44.7
        
    print(f'Seu peso ideal é {resp}kg')

print(f'Numero de participantes: {numPessoas}')
    