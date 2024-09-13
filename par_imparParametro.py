def par_impar (num):
    if (num % 2 == 0):
        return 'PAR'
    else:
        return 'IMPAR'

num = int(input('Digite um numero: '))

resp = par_impar(num);
print(resp)