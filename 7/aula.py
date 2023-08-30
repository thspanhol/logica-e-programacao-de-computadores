# Função simples que imprime uma mensagem:
def greet(name):
    print("Hello, " + name + "!")

greet("Thales")
greet("Spanhol")

print('=' * 30)

# Função com argumentos padrão:
def power(base, exponent=2):
    return base ** exponent

squared = power(4)
cubed = power(2, 3)
print("4^2 =", squared)
print("2^3 =", cubed)

print('=' * 30)

# Função que aceita número variável de argumentos:
def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

sum_result = calculate_sum(2, 4, 6, 8)
print("Soma:", sum_result)

print('=' * 30)

# Função que retorna múltiplos valores:
def min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 9, 1, 6, 5]
minimum, maximum = min_max(nums)
print("Mínimo:", minimum)
print("Máximo:", maximum)

print('=' * 30)

#Função lambda (anônima):
square = lambda x: x ** 2
print(square(4))  # Saída: 16

'''
Mesma coisa que:
def square(x):
    return x ** 2

print(square(4))  # Saída: 16

'''
print('=' * 30)
