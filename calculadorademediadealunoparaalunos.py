print('Olá')
nota1 = float(input('Quanto tirou na primeira nota?:'))
nota2 = float(input('Quanto tirou na segunda prova?:'))
compor = float(input('ficou com quantos na pontos na média?:'))
media_de_alino = nota1 + nota2 + compor / 2
if media_de_alino < 6.0:
    print('Ele/a tirou {}, portantanto não passou.'.format(media_de_alino))
elif media_de_alino >=6.0:
    print('Ele/a tirou {}, portanto passou!'.format(media_de_alino))
perdunga = input('QUER FECHAR MESMO?:')
