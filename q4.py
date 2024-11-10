def ordenar_pilha(pilha):
    pilha_auxiliar = []

    while pilha:
        # Remove o elemento do topo da pilha original
        temp = pilha.pop()

        # Enquanto a pilha auxiliar tiver elementos e o topo for maior que o elemento temporário
        while pilha_auxiliar and pilha_auxiliar[-1] > temp:
            pilha.append(pilha_auxiliar.pop())

        # Coloca o elemento temporário na posição correta na pilha auxiliar
        pilha_auxiliar.append(temp)

    # Transferindo os elementos da pilha auxiliar para a pilha original em ordem crescente
    while pilha_auxiliar:
        pilha.append(pilha_auxiliar.pop())

    return pilha

# Exemplo de pilha de notas de um aluno
notas = [70, 85, 60, 90, 75]

# Ordenando a pilha em ordem crescente
notas_ordenadas = ordenar_pilha(notas)

print("Notas ordenadas:", notas_ordenadas)
