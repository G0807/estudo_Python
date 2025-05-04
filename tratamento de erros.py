try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b
except:
    print('Erro!')
else:
    print(f'O resultado é {r}')    
finally:
    print('Fim!') 
