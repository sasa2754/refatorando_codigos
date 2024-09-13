qtd = 0
while True:
    num = int(input('Digite um numero: '))
    
    if(num == 0):
        break
    
    qtd += 1

print(f'Foram informados {qtd} numeros!')