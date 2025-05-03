def dizimo(valor=0):
	resultado = (valor * 10) / 100
	resultado = resultado + valor
	return resultado



def dobro(valor=0):
    resultado = valor * 2
    return resultado

def metade(valor=0):
    resultado = valor / 2
    return resultado

def moeda(valor=0):
	return f'R$:{valor:>.2f}'.replace('.', ',')

def resultado(valor=0):
    return ( 
        f'O valor de R$:{moeda(valor)} aumentado em 10% é R${moeda(dizimo(valor))}\n'
        f'O dobro de R$:{moeda(valor)} é R$:{moeda(dobro(valor))}\n'
        f'A metade R$:{moeda(valor)} é R$:{moeda(metade(valor))}'
    )

def obter_valor():
    while True:
        try:
            return float(input('Digite o preço de um produto separado por ponto. R$:'))
        except ValueError:
            print('ERRO! Somente números separados por ponto, por favor.')
