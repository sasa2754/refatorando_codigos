hora = 10
horaExtra = 15

horaNormais = int(input('Informe o numero de horas normais trabalhadas no ano:'))
horasExtras = int(input('Informe o numero de horas extras trabalhadas no ano:'))


horaNormalResul = horaNormais * hora
horaExtraResult = horaExtra * horasExtras
result = horaNormalResul * horaExtraResult

poup = result * 0.08

print(f'Valor de horas normais: {horaNormalResul}')
print(f'Valor de horas extras: {horaExtraResult}')
print(f'Total de ganho ao ano: {result}')
print(f'Valor a guardar na poupança: {poup}')


