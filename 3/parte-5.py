numero = int(input('informe um número de 1 a 7 e será informado qual o dia da semana correspondente: '))
dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
if numero >= 1 and numero <= 7 : print(dias[numero - 1])
else : print('Número inválido.')