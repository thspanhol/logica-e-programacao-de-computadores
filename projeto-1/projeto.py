data = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

print('-' * 20)
print('Informe a seguir os meses do ano e suas temperaturas máximas registradas, ao final será demonstrado as estatisticas metereológicas deste mesmo ano.')
print('-' * 20)

while len(data) < 12:
    dataKeys = [list(d.keys())[0] for d in data]
    mes = int(input('Digite o número correspondente a um mês: '))
    if mes in dataKeys:
        print(f'{meses[mes-1]} já foi adicionado aos dados, informe outro mês por favor.')
        continue
    clima = float(input('Digite a temperatura máxima desse mês, utilize ponto para separar os decimais: '))
    if clima < -60 or clima > 50:
        print('A temperatura deve ser informada em Celsius, informe novamente este mês e a temperatura na escala termométrica correta por favor.')
        continue
    data.append({mes: clima})

dataSortValues = sorted(data, key=lambda x: list(x.values())[0])

# Temperatura média anual
mediaAnual = 0.0
for graus in data:
    mediaAnual += list(graus.values())[0]
mediaAnual = int((mediaAnual / 12) * 100) / 100.0

# Array com temperaturas dos meses escaldantes
mesesEscaldantes = [list(d.values())[0] for d in data if list(d.values())[0] > 38]

# Mês mais frio e sua temperatura
mesMaisFrio, menorTemperatura = list(dataSortValues[0].items())[0]

# Mês mais quente e sua temperatura
mesMaisQuente, maiorTemperatura = list(dataSortValues[len(dataSortValues) - 1].items())[0]

print('Obrigado pelas informações!')
print('RESULTADOS:')
print('=' * 10)
print('Temperatura média anual: ', mediaAnual)
print('-' * 20)
print('Quantidade de meses escaldantes: ', len(mesesEscaldantes))
print('-' * 20)
print(f'{meses[mesMaisQuente - 1]} foi o mês mais quente do ano, com {maiorTemperatura} graus.')
print('-' * 20)
print(f'{meses[mesMaisFrio - 1]} foi o mês mais frio do ano, com {menorTemperatura} graus.')
print('-' * 20)