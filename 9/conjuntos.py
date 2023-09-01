'''
Em Python, um conjunto é uma coleção não ordenada de elementos únicos. Os conjuntos são usados quando você quer armazenar um grupo de valores sem se preocupar com a ordem e deseja garantir que não haja duplicatas. Eles são muito eficientes para verificar a existência de um elemento em uma coleção e também para realizar operações de conjunto, como união, interseção e diferença.

Sintaxe de um conjunto:

Conjuntos são definidos usando chaves {} ou a função set(). Os elementos são separados por vírgulas.
'''
# Exemplo de criação de um conjunto
frutas = {"maçã", "banana", "laranja"}

# Verificando existência de elementos:
if "banana" in frutas:
    print("Banana está no conjunto.")

# Adicionando elementos:
frutas.add("uva")
print(frutas)  # Saída: {'maçã', 'laranja', 'banana', 'uva'}

# Removendo elementos:
frutas.remove("maçã")
print(frutas)  # Saída: {'laranja', 'banana', 'uva'}

# Operações de conjunto:
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

# União
uniao = conjunto1.union(conjunto2)
print(uniao)  # Saída: {1, 2, 3, 4, 5, 6}

# Interseção
intersecao = conjunto1.intersection(conjunto2)
print(intersecao)  # Saída: {3, 4}

# Diferença
diferenca = conjunto1.difference(conjunto2)
print(diferenca)  # Saída: {1, 2}

# Iterando sobre um conjunto:
for fruta in frutas:
    print(fruta)

# Convertendo uma lista em um conjunto (removendo duplicatas):
lista_com_duplicatas = [1, 2, 3, 2, 1, 4]
conjunto_sem_duplicatas = set(lista_com_duplicatas)
print(conjunto_sem_duplicatas)  # Saída: {1, 2, 3, 4}

'''
Conjuntos são úteis quando você precisa armazenar valores únicos e deseja realizar operações de conjunto eficientes. No entanto, lembre-se de que os conjuntos não mantêm uma ordem específica dos elementos.
'''

'''
--Diferença entre Dicionários e Conjuntos:

Tanto dicionários quanto conjuntos são estruturas de dados em Python que permitem armazenar elementos, mas eles têm algumas diferenças significativas:

Elementos e Estrutura:

 Dicionários: São coleções de pares chave-valor, onde cada chave é única e associada a um valor específico. As chaves em um dicionário são imutáveis (geralmente strings ou números) e os valores podem ser de qualquer tipo.

 Conjuntos: São coleções de elementos únicos, onde a ordem dos elementos não é relevante. Os elementos de um conjunto são apenas valores individuais, e não há associação entre chaves e valores.

Acesso e Indexação:

 Dicionários: Os elementos em um dicionário são acessados por meio de suas chaves, usando a sintaxe dicionario[chave]. Isso permite um acesso eficiente aos valores com base em um rótulo específico.

 Conjuntos: Os elementos em um conjunto são acessados apenas para verificação de existência usando o operador in.

Duplicatas:

 Dicionários: As chaves em um dicionário são únicas, mas os valores podem se repetir.

 Conjuntos: Contêm apenas elementos únicos, sem repetições.

Mutabilidade:

 Dicionários: São mutáveis, o que significa que você pode adicionar, remover ou alterar pares chave-valor após a criação do dicionário.

 Conjuntos: Também são mutáveis, permitindo adicionar e remover elementos.

Uso Principal:

 Dicionários: São usados para associar informações relacionadas a uma chave específica, como um registro de informações sobre um objeto ou entidade.
 
 Conjuntos: São usados quando você quer armazenar uma coleção de elementos únicos e deseja verificar a existência de elementos eficientemente.

Em resumo, a principal diferença entre dicionários e conjuntos é a forma como os elementos são armazenados e acessados. Dicionários usam pares chave-valor para associar informações, enquanto conjuntos armazenam elementos únicos, sem uma associação direta. Ambas as estruturas têm suas aplicações específicas e são valiosas para resolver diferentes tipos de problemas.
'''