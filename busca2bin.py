vet = []

for i in range(10):
    vet.append(int(input(f'Informe o {i+1}° valor: ')))
    
busca = int(input('Informe um valor para ser procurado: '))

achou = 0
baixo = 0
alto = 9

while(baixo <= alto and achou == 0):
    medio = (baixo + alto)/2
    medio = int(medio)
    
    if(busca < vet[medio]):
        alto = medio + 1
    else:
        if busca > vet[medio]:
            baixo = medio + 1
        else:
            achou = 1


if(achou == 1):
    print('Foi encontrado!')

else:
    print('Não foi encontrado!')