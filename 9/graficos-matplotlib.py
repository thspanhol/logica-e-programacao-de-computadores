'''
Matplotlib é uma biblioteca de visualização em Python que permite criar uma variedade de gráficos, plots, gráficos de dispersão, histogramas, gráficos de contorno e muito mais. Ela é amplamente utilizada para visualização de dados e geração de gráficos de alta qualidade em diferentes formatos.
'''

import matplotlib.pyplot as plt

#  -- Exemplo de Gráfico de Linhas:

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Criar o gráfico de linhas
plt.plot(x, y, label='y = 2x', color='blue', marker='o')

# Adicionar rótulos e título
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Linhas')
plt.legend()

# Mostrar o gráfico
plt.show()

#  -- Exemplo de Gráfico de Barras:

# Dados para o gráfico
categorias = ['A', 'B', 'C', 'D']
valores = [10, 30, 20, 40]

# Criar o gráfico de barras
plt.bar(categorias, valores, color='green')

# Adicionar rótulos e título
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')

# Mostrar o gráfico
plt.show()

#  -- Exemplo de Gráfico de Dispersão:

# Dados para o gráfico de dispersão
x = [1, 2, 3, 4, 5]
y = [3, 6, 2, 8, 4]

# Criar o gráfico de dispersão
plt.scatter(x, y, color='red', marker='x', label='Pontos')

# Adicionar rótulos e título
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Dispersão')
plt.legend()

# Mostrar o gráfico
plt.show()

'''
Esses são apenas exemplos simples de como usar o Matplotlib para criar diferentes tipos de gráficos. A biblioteca oferece uma ampla gama de opções de personalização para criar gráficos visualmente atraentes e informativos. Ela é uma ferramenta poderosa para a visualização de dados e é frequentemente usada em análises de dados, ciência de dados e apresentações de informações. Certifique-se de instalar o Matplotlib usando o comando pip install matplotlib antes de tentar executar esses exemplos.
'''