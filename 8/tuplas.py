'''
Tuplas:

Uma tupla é uma coleção ordenada e imutável de elementos, separados por vírgulas e 
geralmente delimitados por parênteses. Uma vez que uma tupla é criada, seus elementos 
não podem ser alterados, adicionados ou removidos. As tuplas são usadas quando você deseja 
agrupar diferentes elementos de maneira ordenada, mas não pretende modificá-los.
'''
# Criando uma tupla
point = (3, 4)
coordinates = (10, 20, 30)

# Acessando elementos da tupla
x = point[0]  # x é igual a 3

# Desempacotamento de tuplas
x, y = point  # x é igual a 3, y é igual a 4

'''
Diferenças entre tuplas e listas:

 Mutabilidade:
- As tuplas são imutáveis, ou seja, uma vez que você cria uma tupla, 
não pode alterar seus elementos individualmente.
- As listas são mutáveis, permitindo adicionar, remover e modificar elementos após a criação.

 Sintaxe:
- As tuplas são geralmente delimitadas por parênteses, mas os parênteses são opcionais na 
maioria dos casos.
- As listas são delimitadas por colchetes.

 Uso:
- Use tuplas quando você quer garantir que os elementos não serão alterados e deseja garantir 
a integridade dos dados.
- Use listas quando você precisa de uma estrutura de dados flexível que possa ser modificada.

 Desempenho:
- Em algumas situações, as tuplas podem ser mais eficientes em termos de desempenho do que as 
listas devido à sua imutabilidade.

 Em resumo, escolha entre tuplas e listas com base na necessidade de mutabilidade dos 
elementos e no uso específico que você pretende dar a eles. Se precisar alterar os elementos, 
use listas. Se quiser garantir a imutabilidade dos elementos, use tuplas.
'''