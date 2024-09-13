def funcao(n1 , nxn1):
    if(nxn1 == 1):
        return n1
    else:
        return n1 + funcao(n1, nxn1-1)

n1 = int(input('Informe o primeiro número: '))
nxn1 = int(input('Informe o número de vezes que o número anterior será somado: '))
resp = funcao(n1, nxn1)

print('Resposta: ', resp)