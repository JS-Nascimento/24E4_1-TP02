def contar_livros_impares(fila_livros):
    contador_impares = 0
    for id_livro in fila_livros:
        if id_livro % 2 != 0:  # Verifica se o número de identificação é ímpar
            contador_impares += 1
    return contador_impares

# Exemplo de fila de livros com números de identificação
fila_livros = [1023, 1024, 1025, 1026, 1027]

# Chamando a função para contar livros com identificações ímpares
quantidade_impares = contar_livros_impares(fila_livros)
print("Quantidade de livros com identificação ímpar:", quantidade_impares)  # Deve exibir 3
