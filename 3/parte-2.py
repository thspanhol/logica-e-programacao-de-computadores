altura = float(input('informe sua altura: '))
genero = int(input('informe seu genero, usando 1 para feminino e 2 para masculino: '))
if genero == 1 : peso = 62.1 * altura - 44.7
if genero == 2 : peso = 72.7 * altura - 58
if genero != 1 and genero != 2 :
    print('genero invalido, peso ideal não calculado')
    peso = 'não calculado'
print('peso ideal: ', peso)