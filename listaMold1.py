def calculo(precoLitro, valorPgto):
    res = valorPgto / precoLitro
    return res

nome = input('Digite seu nome: ')
precoLitro = float(input('Informe o valor por litro de gasolina: '))

valorPgto = float(input('Informe o valor de pagamento: '))

res = calculo(precoLitro, valorPgto)
print(f'{nome}, você vai abastecer {round(res, 2)} por litro de gasolina.')
