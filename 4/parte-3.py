mes = int(input('Digite o número do mês para saber quantos dias ele possui: '))
if mes == 2 : dias = 28
elif mes in [4, 6, 9, 11] : dias = 30
else : dias = 31
print(f'Esse mês possui {dias} dias.')