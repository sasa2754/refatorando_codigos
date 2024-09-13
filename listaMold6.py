def Calculo(peq, med, grand, name):
    
    respP = peq * 10
    respM = med * 12
    respG = grand * 15
    
    print(f'{name}, o valor arrecadado foi de: R${round(float(respP + respM + respG), 2)}')
    
print('LOJA DE CAMISETA')
peq = int(input('Qual é a qtd de camisetas P? (R$10,00): '))
med = int(input('Qual é a qtd de camisetas M? (R$12,00): '))
grand = int(input('Qual é a qtd de camisetas G? (R$15,00): '))

nome = input('Qual é seu nome?\n')

Calculo(peq, med, grand, nome)
