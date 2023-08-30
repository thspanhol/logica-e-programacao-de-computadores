# Usando o método append() para adicionar um elemento ao final da lista
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Saída: [1, 2, 3, 4]

# Usando o método insert() para inserir um elemento em uma posição específica
numbers.insert(1, 5)  # Insere o número 5 na posição 1
print(numbers)  # Saída: [1, 5, 2, 3, 4]

# Usando o método remove() para remover o primeiro elemento com um valor específico
numbers.remove(2)
print(numbers)  # Saída: [1, 5, 3, 4]

# Usando a instrução del para remover um elemento em uma posição específica
del numbers[0]  # Remove o elemento na posição 0
print(numbers)  # Saída: [5, 3, 4]

# Usando índices positivos e negativos para acessar elementos
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])    # Saída: "apple"
print(fruits[-1])   # Saída: "date"

# Usando um loop for para iterar sobre os elementos da lista
for fruit in fruits:
    print(fruit)

# Usando enumerate() para obter índices enquanto itera
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Usando o método sort() para ordenar a lista
numbers = [4, 2, 1, 3]
numbers.sort()
print(numbers)  # Saída: [1, 2, 3, 4]

# Usando o método reverse() para reverter a lista
numbers.reverse()
print(numbers)  # Saída: [4, 3, 2, 1]

# Usando list comprehension para criar uma nova lista
squares = [x ** 2 for x in range(5)]
print(squares)  # Saída: [0, 1, 4, 9, 16]

# Usando list comprehension para filtrar elementos
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Saída: [4, 2]

# Usando o operador in para verificar a presença de um elemento
if "banana" in fruits:
    print("Banana está na lista!")

# Modificando elementos da lista
numbers[0] = 0