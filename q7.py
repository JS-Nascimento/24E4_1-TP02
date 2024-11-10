def contar_pedidos_pares(pilha_de_pedidos):
    contador_pares = 0
    for pedido in pilha_de_pedidos:
        if pedido % 2 == 0:  # Verifica se o número de identificação é par
            contador_pares += 1
    return contador_pares

# Exemplo de pilha de pedidos
pilha_de_pedidos = [1023, 1024, 1025, 1026, 1027]

# Chamando a função para contar pedidos pares
quantidade_pares = contar_pedidos_pares(pilha_de_pedidos)
print("Quantidade de pedidos com número par:", quantidade_pares)  # Deve exibir 2
