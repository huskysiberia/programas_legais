import random
print('Olá')
predununca = input('Quer criar uma senha?')
if predununca == 'não':
    exit()
else:
    letrasmin = 'abcdefghijklmnopqrstuvwxyz'
    letrasmai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '1234567890'
    simbolo = '!@#$%_-¨&*'
    possiveis = letrasmin + letrasmai + num + simbolo

    senha = ''.join(random.sample(possiveis, 10))

    print('A senha gerada foi:{}'.format(senha))
    pregunta = input('QUER FECHAR MESMO?:')

