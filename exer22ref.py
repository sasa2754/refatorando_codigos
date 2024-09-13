def imprime (numeroInt):
    print(f'Numero digitado: {numeroInt}')

num = int(input('Informe um número inteiro: '))

if type(num) == float: #Nem tem como entrar aqui, pq ele da erro, mas vai q né kskaskakssk
    print('NÚMERO INTEIROOOOOOOOOOOOOOO!')
else:
    imprime(num)
    