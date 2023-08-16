'''
inicio = float(input('informe o horário de inicio do jogo: '))
final = float(input('informe o horário do final do jogo: '))
if final > inicio : tempo = final - inicio
else : tempo = (24 - inicio) + final
print('Tempo do jogo: ', tempo)
'''
numero = int(input('informe um número de 4 digitos: '))
emString = str(numero)
invertido = emString[::-1]
if emString == invertido : print('Os números digitados são um capicua')
else : print('Os números digitados NÃO são um capicua')