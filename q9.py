def ordenar_fila(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                # Troca os elementos se o anterior é maior que o próximo
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# Exemplo de fila de números inteiros
fila_numeros = [5, 3, 8, 4, 2]

# Ordenando a fila em ordem crescente
fila_ordenada = ordenar_fila(fila_numeros)
print("Fila ordenada:", fila_ordenada)
