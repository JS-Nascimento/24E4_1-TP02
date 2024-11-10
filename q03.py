def encontrar_duplicados_forca_bruta(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados

def encontrar_duplicados_com_set(lista):
    vistos = set()
    duplicados = set()
    for numero in lista:
        if numero in vistos:
            duplicados.add(numero)
        else:
            vistos.add(numero)
    return list(duplicados)

lista = [1, 2, 3, 4, 5, 3, 6, 7, 8, 2, 9, 10, 1]

# Usando força bruta
print("Duplicados (Força Bruta):", encontrar_duplicados_forca_bruta(lista))

# Usando set para melhorar a eficiência
print("Duplicados (Set):", encontrar_duplicados_com_set(lista))
