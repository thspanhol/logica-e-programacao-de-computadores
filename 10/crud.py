# Lista de dicionários para armazenar registros
registros = []

# Função para criar um novo registro
def criar_registro(nome, idade):
    registro = {'nome': nome, 'idade': idade}
    registros.append(registro)
    return "Registro criado com sucesso."

# Função para ler todos os registros
def ler_registros():
    return registros

# Função para ler um registro específico pelo nome
def ler_registro_por_nome(nome):
    for registro in registros:
        if registro['nome'] == nome:
            return registro
    return "Registro não encontrado."

# Função para atualizar um registro pelo nome
def atualizar_registro(nome, nova_idade):
    for registro in registros:
        if registro['nome'] == nome:
            registro['idade'] = nova_idade
            return "Registro atualizado com sucesso."
    return "Registro não encontrado."

# Função para deletar um registro pelo nome
def deletar_registro(nome):
    for registro in registros:
        if registro['nome'] == nome:
            registros.remove(registro)
            return "Registro deletado com sucesso."
    return "Registro não encontrado."

# Exemplo de uso do CRUD
criar_registro("Alice", 25)
criar_registro("Bob", 30)

print("Registros iniciais:")
print(ler_registros())

atualizar_registro("Alice", 26)
print("Registro atualizado:")
print(ler_registro_por_nome("Alice"))

deletar_registro("Bob")
print("Registros após exclusão:")
print(ler_registros())
