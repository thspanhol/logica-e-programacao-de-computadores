num1 = 7
num2 = 3
num3 = 4
'''num3 está no intervalo entre 0 e 10'''
print(num3 >= 0 and num3 <= 10)
'''num1 não está no intervalo entre 0 e 10'''
print(num1 < 0 or num1 > 10)
'''num2 é o maior dos 3 valores'''
print(num2 > num1 and num2 > num3)
'''num2 é divisivel por 7'''
print(num2 % 7 == 0)
'''num2 e num3 são multiplos'''
print(num2 % num3 == 0 or num3 % num2 == 0)
'''os 3 valores são iguais'''
print(num1 == num2 and num2 == num3)
'''2 dos 3 valores são iguais'''
print(num1 == num2 or num2 == num3 or num3 == num1)