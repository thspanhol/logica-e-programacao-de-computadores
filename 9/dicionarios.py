'''
Em Python, um dicionário é uma estrutura de dados que permite armazenar e organizar elementos em pares de chave-valor. Cada elemento é acessado através de sua chave, e as chaves em um dicionário são únicas. Dicionários são úteis para armazenar informações associadas a um determinado valor descritivo, como um índice ou um identificador.

Sintaxe de um dicionário:

Um dicionário é definido usando chaves {} e pares chave-valor separados por dois pontos :. As chaves são usadas para acessar os valores correspondentes.
'''
# Exemplo de um dicionário
person = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "Cidade Exemplo"
}

# Acessando valores:
print(person["nome"])  # Saída: "Alice"
print(person["idade"])  # Saída: 30

# Alterando valores:
person["idade"] = 31
print(person["idade"])  # Saída: 31

# Adicionando novos pares chave-valor:
person["profissao"] = "Engenheira"
print(person)  # Saída: {'nome': 'Alice', 'idade': 31, 'cidade': 'Cidade Exemplo', 'profissao': 'Engenheira'}

# Removendo pares chave-valor:
del person["cidade"]
print(person)  # Saída: {'nome': 'Alice', 'idade': 31, 'profissao': 'Engenheira'}

# Verificando a existência de uma chave:
if "profissao" in person:
    print("Chave 'profissao' existe no dicionário.")

# Iterando sobre chaves e valores:
for key in person:
    print(key, person[key])

# Ou usando o método items()
for key, value in person.items():
    print(key, value)

'''
Dicionários são muito flexíveis e podem ser usados para representar informações complexas em Python. Eles são ideais para casos em que você precisa armazenar informações associadas a identificadores ou rótulos.
'''