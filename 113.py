def leiaint():
    while True:
        try:
            numero = int(input('Digite um numero inteiro: '))
            break
        except:
            print('ERR0! Digite um número inteiro valido.')
def leiafloat():
    while True:
        try:
            numero = float(input('Digite um número real, separado somente por ponto. '))
            break
        except:
            print('Digite um número Real valido: ')

leiaint()
leiafloat()
