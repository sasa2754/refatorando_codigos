totalSexof21 = 0
totalF = 0
totalSexom18 = 0
totalM = 0
totalSexof = 0
totalSexom = 0

for i in range(3):
    idade = int(input('Qual é a idade: '))
    sexo = input('Qual é o sexo (M/F): ')
    
    sexo = sexo.upper()
    
    if idade >= 21 and sexo == 'F':
        totalSexof21 += 1
        totalF += idade
        
    elif sexo == 'F':
        totalSexof += 1
        totalF == idade
    
    elif idade >= 18 and sexo == 'M':
        totalSexom18 += 1
        totalM += idade
    
    elif sexo == 'M':
        totalSexom += 1
        totalM += idade
        
if(totalSexof != 0):
    mediaF = totalF/(totalSexof + totalSexof21)
    print(f'Media de idade de sexo feminino é de: {mediaF}')

if(totalSexom != 0):
    mediaM = totalM/(totalSexom + totalSexom18)
    print(f'Media de idade do sexo masculino é de: {mediaM}')
    
    
print(f'Total do sexo feminino e maior que 21 anos: {totalSexof21}')
print(f'Total do sexo masculino e maior que 18 anos: {totalSexom18}')