def contar_pedidos_impares(pilha_de_pedidos):
    contador_impares = 0
    for pedido in pilha_de_pedidos:
        if pedido % 2 != 0:  # Verifica se o número de identificação é ímpar
            contador_impares += 1
    return contador_impares

# Exemplo de pilha de pedidos
pilha_de_pedidos = [1023, 1024, 1025, 1026, 1027]

# Chamando a função para contar pedidos ímpares
quantidade_impares = contar_pedidos_impares(pilha_de_pedidos)
print("Quantidade de pedidos com número ímpar:", quantidade_impares)  # Deve exibir 3
