# Sintaxe:
# variavelArquivo = open(nomeArquivo, proposito)
# r = Leitura || w = Gravação || a = Alteração append, Acrescenta ao final

'''
 Exemplo Ler:

arq = open('nome-do-arquivo', 'r')
for linha in arq:
    print(linha)
arq.close()

Deve-se fechar o arquivo sempre que o abrir.

 Exemplo Gravar:

ref_arquivo = open('nome-do-arquivo', 'w') # Seria 'a' no lugar do 'w' para dicionar novas linhas ao final das existentes.
cont = 1
while cont <= 3:
    nome = input('Informe o nome: ')
    ref_arquivo.write(nome + '\n')
    cont = cont + 1
ref_arquivo.close()
'''