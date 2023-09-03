from collections import defaultdict
import matplotlib.pyplot as plt

# Define os futuros bancos de dados
bigData = []
precipData = []
tempData = []
umveData = []
minTempData = []

# Faz a leitura do arquivo e salva as informações nos bancos criados para cada futura situação
arq = open('Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv', 'r')

for linha in arq:
    db = linha.split(',')
    day = {
        'data': db[0],
        'precip': db[1],
        'maxima': db[2],
        'minima': db[3],
        'horas_insol': db[4],
        'temp_media': db[5],
        'um_relativa': db[6],
        'vel_vento': db[7].replace('\n', ''),
    }
    onlyPrecip = {
        'data': db[0],
        'precip': db[1],
    }
    onlyTemp = {
        'data': db[0],
        'maxima': db[2],
        'minima': db[3],
        'horas_insol': db[4],
        'temp_media': db[5],
    }
    onlyUmve = {
        'data': db[0],
        'um_relativa': db[6],
        'vel_vento': db[7].replace('\n', ''),
    }
    onlyMin = {
        'data': db[0],
        'minima': db[3],
    }
    bigData.append(day)
    precipData.append(onlyPrecip)
    tempData.append(onlyTemp)
    umveData.append(onlyUmve)
    minTempData.append(onlyMin)
arq.close()

# Cria uma lista com os anos permitidos para pesquisa
validYears = [str(ano) for ano in range(1961, 2017)]

print('REQUISITO A:')

# Coleta e valida os dados passados pelo usuário
print('Informe o mês e ano (no formato MM e AAAA) que você deseja iniciar a pesquisa de dados:')
monthIni = input('Mês: ')
while not monthIni in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] :
    print('O mês deve ser um inteiro entre 01 e 12 no formato MM.')
    monthIni = input('Mês: ')
yearIni = input('Ano: ')
while not yearIni in validYears :
    print('O ano deve ser entre 1961 e 2016 no formato AAAA.')
    yearIni = input('Ano: ')

while int(monthIni) > 7 and yearIni == '2016':
    print('Temos dados de 01/1961 até 07/2016, escolha um período entre essas datas.')
    monthIni = input('Mês: ')
    while not monthIni in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] :
        print('O mês deve ser um inteiro entre 01 e 12 no formato MM.')
        monthIni = input('Mês: ')
    yearIni = input('Ano: ')
    while not yearIni in validYears :
        print('O ano deve ser entre 1961 e 2016 no formato AAAA.')
        yearIni = input('Ano: ')

print('Informe o mês e ano (no formato MM e AAAA) que você deseja encerrar a pesquisa de dados:')
monthFin = input('Mês: ')
while not monthFin in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] :
    print('O mês deve ser um inteiro entre 01 e 12 no formato MM.')
    monthFin = input('Mês: ')
yearFin = input('Ano: ')
while not yearFin in validYears or int(yearFin) < int(yearIni):
    print('O ano de encerramento deve ser maior que o de início, e estar entre 1961 e 2016 no formato AAAA.')
    yearFin = input('Ano: ')
while yearFin == yearIni and int(monthIni) > int(monthFin):
    print('Nos casos em que o ano de início e de encerramento da pesquisa forem o mesmo, o mês de encerramento deve ser posterior ou igual ao de início.')
    monthFin = input('Mês: ')

while int(monthFin) > 7 and yearFin == '2016':
    print('Temos dados de 01/1961 até 07/2016, escolha um período entre essas datas.')
    monthFin = input('Mês: ')
    while not monthFin in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] :
        print('O mês deve ser um inteiro entre 01 e 12 no formato MM.')
        monthFin = input('Mês: ')
    yearFin = input('Ano: ')
    while not yearFin in validYears or int(yearFin) < int(yearIni):
        print('O ano de encerramento deve ser maior que o de início, e estar entre 1961 e 2016 no formato AAAA.')
        yearFin = input('Ano: ')
    while yearFin == yearIni and int(monthIni) > int(monthFin):
        print('Nos casos em que o ano de início e de encerramento da pesquisa forem o mesmo, o mês de encerramento deve ser posterior ou igual ao de início.')
        monthFin = input('Mês: ')

print('- Digite 1 para ver todos os dados')
print('- Digite 2 para ver apenas os dados de precipitação')
print('- Digite 3 para ver apenas os dados de temperatura')
print('- Digite 4 para ver apenas os dados de umidade e vento')
choice = input('Quais dados deseja ver? ')
while not choice in ['1', '2', '3', '4'] :
    print('Opção inválida!')
    print('- Digite 1 para ver todos os dados')
    print('- Digite 2 para ver apenas os dados de precipitação')
    print('- Digite 3 para ver apenas os dados de temperatura')
    print('- Digite 4 para ver apenas os dados de umidade e vento')
    choice = input('Quais dados deseja ver? ')

# Define qual banco de dados será usado, de acordo com a escolha do usuário
if choice == '1' : choice = bigData
if choice == '2' : choice = precipData
if choice == '3' : choice = tempData
if choice == '4' : choice = umveData

# Define qual será o primeiro e o último dia filtrado pelo usuário
firstDayFilter = None
for d in choice:
    if f'{monthIni}/{yearIni}' in d['data']:
        firstDayFilter = d
        break

lastDayFilter = None
for d in reversed(choice):
    if f'{monthFin}/{yearFin}' in d['data']:
        lastDayFilter = d
        break

# Função que usa o primeiro e último dia do filtro para resgatar todos os dados entre eles
def filterTime(data, paramIni, paramFin ):
    filterData = []
    coletando = False

    for d in data:
        if d == paramIni:
            coletando = True
            continue

        if coletando:
            if d == paramFin:
                break
            filterData.append(d)

    filterData.append(paramFin)
    filterData.insert(0,paramIni)
    return filterData

print('=' * 30)
# Printa uma frase personalizada para cada dia do período pesquisado
for day in filterTime(choice, firstDayFilter, lastDayFilter):

    if choice == bigData : print(f'No dia {day["data"]} a precipitação foi de {day["precip"]}, a temperatura máxima foi de {day["maxima"]}°C, a mínima foi de {day["minima"]}°C, tivemos {day["horas_insol"]} de horas insol, a temperatura média foi de {day["temp_media"]}°C, a umidade relativa foi de {day["um_relativa"]} e a velocidade do vento foi de {day["vel_vento"]}.')

    if choice == precipData : print(f'No dia {day["data"]} a precipitação foi de {day["precip"]}.')

    if choice == tempData :print(f'No dia {day["data"]} a temperatura máxima foi de {day["maxima"]}°C, a mínima foi de {day["minima"]}°C, tivemos {day["horas_insol"]} de horas insol e a temperatura média foi de {day["temp_media"]}°C.')

    if choice == umveData : print(f'No dia {day["data"]} a umidade relativa foi de {day["um_relativa"]} e a velocidade do vento foi de {day["vel_vento"]}.')

print('=' * 30)
print('REQUISITO B:')

# Função que recebe os dados de precip como parametro pra calcular o valor mensal, ordena de forma crescente e retorna o primeiro item da lista (menor valor)
def smallerPrecip(paramData):
    soma_precip_por_mes_ano = {}

    for registro in paramData:
        partes_data = registro['data'].split('/')
        if len(partes_data) == 3:
            dia, mes, ano = partes_data

            chave = f'{mes}/{ano}'
            precipitacao = float(registro['precip'])
        
            soma_precip_por_mes_ano[chave] = soma_precip_por_mes_ano.get(chave, 0) + precipitacao

    monthlyPrecip = []
    for chave, soma in soma_precip_por_mes_ano.items():
        monthlyPrecip.append({'data': chave, 'precip': soma})

    sortPrecip = sorted(monthlyPrecip, key=lambda x: x['precip'])

    return sortPrecip[0]

monthLessRain = smallerPrecip(precipData)

print(f'Você sabia que o mês menos chuvoso já registrado foi em {monthLessRain["data"]}? A soma de precipitação TOTAL do mês foi {monthLessRain["precip"]}!')

print('=' * 30)
print('REQUISITO C:')

# Recebe e valida o mês escolhido pelo usuário
print('Digite um mês do ano no formato MM para descobrir a média da temperatura mínima desse mês pelo período de 2006 até 2016:')
monthMinTemp = input('Mês: ')
while not monthMinTemp in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] :
    print('O mês deve ser um inteiro entre 01 e 12 no formato MM.')
    monthMinTemp = input('Mês: ')

# Função recebe os dados com a data e temperatura mínima além do mês escolhido pelo usuário como parâmetros, calcula a média da mínima do mês em cada ano partindo de zero e retorna essas informações em uma lista
def calculateMinimum(dados, paramMes):
    soma_minima_por_mes = defaultdict(float)
    
    contagem_por_mes = defaultdict(int)
    
    for registro in dados:
        partes_data = registro['data'].split('/')
        if len(partes_data) == 3:
            dia, mes, ano = partes_data
            chave = f'{mes}/{ano}'
            temperatura_minima = float(registro['minima'])
            soma_minima_por_mes[chave] += temperatura_minima
            contagem_por_mes[chave] += 1
    
    media_minima_por_mes = {}
    for chave, soma in soma_minima_por_mes.items():
        media_minima = soma / contagem_por_mes[chave]
        media_minima_por_mes[chave] = media_minima
    
    minScore = []

    for chave, media in media_minima_por_mes.items():
        if chave in [f'{paramMes}/2006', f'{paramMes}/2007', f'{paramMes}/2008', f'{paramMes}/2009', f'{paramMes}/2010', f'{paramMes}/2011', f'{paramMes}/2012', f'{paramMes}/2013', f'{paramMes}/2014', f'{paramMes}/2015', f'{paramMes}/2016']:
            minScore.append({'data': chave, 'minima': "{:.2f}".format(round(media, 2))})

    return minScore

calculatedTempMin = calculateMinimum(minTempData, monthMinTemp)

# Printa o mês escolhido em cada ano
for ano in calculatedTempMin:
    print(f'Em {ano["data"]} a média da temperatura mínima foi {ano["minima"]}')

# Calcula a média mínima dos meses somando os valores e dividindo pelo número de itens na lista
soma_minimas = 0

for mes in calculatedTempMin:
    valor_minima = float(mes['minima'])
    soma_minimas += valor_minima

media_minimas = soma_minimas / len(calculatedTempMin)

print(f'E a média das temperaturas mínimas do mês {monthMinTemp} ao longo desses anos é {media_minimas:.2f}!')

print('=' * 30)
print('REQUISITO D:')
print('Veja o gráfico com esses dados:')

# Dados para elaboração do gráfico
minDataList = [mes['data'] for mes in calculatedTempMin]
minTempList = [float(temp['minima']) for temp in calculatedTempMin]

# Cria o gráfico de barras
plt.bar(minDataList, minTempList, color='blue')

# Adiciona rótulos e título
plt.xlabel('Mês/Ano')
plt.ylabel('Temperatura mínima')
plt.title(f'Média da temperatura mínima do mês {monthMinTemp} nos últimos anos')

# Mostra o gráfico
plt.show()