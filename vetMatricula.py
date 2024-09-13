vetMatricula = []
busca = 0
achado = 0

for i in range (5):
    vetMatricula.append(int(input('Digite o numero da matricula: ')))
    
busca = int(input('Informe a matricula para ser consultada: '))

for j in range(5):
    if busca == vetMatricula[j]:
        achado = 1
        break
    
if achado == 1:
    print('Matricula encontrada!')
else:
    print('Matricula não encontrada!')