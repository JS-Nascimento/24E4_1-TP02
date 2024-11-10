def tarefa_no_topo(pilha_de_tarefas):
    if not pilha_de_tarefas:
        return None  # Retorna None se a pilha estiver vazia
    return pilha_de_tarefas[-1]  # Retorna o elemento do topo sem removê-lo

# Exemplo de pilha de tarefas
pilha_de_tarefas = ["Tarefa 1", "Tarefa 2", "Tarefa 3"]

# Obtendo a tarefa mais recente
tarefa_recente = tarefa_no_topo(pilha_de_tarefas)
print("Tarefa no topo:", tarefa_recente)  # Deve exibir "Tarefa 3"

# Verificando que a tarefa ainda está na pilha
print("Pilha de tarefas:", pilha_de_tarefas)  # Deve exibir ["Tarefa 1", "Tarefa 2", "Tarefa 3"]
