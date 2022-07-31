print('Olá')
pergunta = input('Quer usar esse programa mesmo?Se quiser digite 1 se não quiser digite 2:')
if pergunta == '2':
    print('Finalizando o sistema....')
    exit()
if pergunta =='1':
    pare1 = float(input('Qual a largura da sua parede?:'))
    pare2 = float(input('Qual a altura da sua parede?:'))
    matrocubi = float(input('Quantos metros cúbicos da para pintar com uma tinta?:'))
    area = pare1 * pare2
    preço = float(input('Quantos reais e a tinta R$'))
    yeni = area * preço / matrocubi
    print('esta e a área da sua parede:{} e você ira gastar {:.3f}.'.format(area,yeni))
perdunta = input('QUER FECHAR MESMO?:')
exit()
