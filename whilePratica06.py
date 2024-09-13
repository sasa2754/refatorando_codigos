idade = 1
contAdul = 0
contTotal = 0
contIA = 0
contIB = 0
contJA = 0
contJB = 0

while idade > 0:
    
    idade = int(input('Digite a idade do nadador ou 0 para sair: '))

    if idade >= 18:
        contAdul += 1
        contTotal += 1
        print('Adulto')
        
    elif idade >= 5 and idade <= 7:
        contIA += 1
        contTotal += 1
        print('Infantil A')
        
    elif idade >= 8 and idade <= 10:
        contIB += 1
        contTotal += 1
        print('Infantil B')
    
    elif idade >= 11 and idade <= 13:
        contJA += 1
        contTotal += 1
        print('Juvenil A')
        
    elif idade >= 14 and idade <= 17:
        contJB += 1
        contTotal += 1
        print('Juvenil B')
        
print(f'Categoria infantil A são: {contIA}')
print(f'Categoria infantil B são: {contIB}')
print(f'Categoria juvenil A são: {contJA}')
print(f'Categoria juvenil B são: {contJB}')
print(f'Categoria adultos são: {contAdul}')

print(f'Total: {contTotal}')




