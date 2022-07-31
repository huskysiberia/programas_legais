print('Olá')
peso = float(input('Qual seu peso?(Kg):'))
altatura = float(input('Qual sua altura?(Ex:1.34):'))
IMC = peso / (altatura ** 2)
if IMC < 18.5:
    print('Seu  IMC é de {:.1f}, você está na faixa de abaixo do peso, coma mais arroz é feijão!'.format(IMC))
elif 18.5 >= IMC < 25:
    print('Seu IMC é de {:.1f}, você está na faixa de peso normal, Parabéns comtinue com esse hábito saudável!'.format(IMC))
elif 25 >= IMC < 30:
    print('Seu IMC é de {:.1f}, você está na faixa de sobre peso, começe sua vida saudável!'.format(IMC))
elif 30 >= IMC < 40:
    print('seu IMC é de {:.1f}, você está na faixa de obesidade fase 1, tenha um hábito sáudavel urgente!'.format(IMC))
elif 40 >= IMC < 55:
    print('Seu IMC é de {:.1f}, você está na faixa de obesidade fase 2, vá para a academia!'.format(IMC))
elif IMC >= 55:
    print('Seu IMC é de {:.1f47}, você está na faixa de obesidade fase 3, consulte um médico.')
pergunta = input('Gostou deste programa?:')
exit()