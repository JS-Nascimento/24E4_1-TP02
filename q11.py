class FilaAtendimento:
    def __init__(self):
        self.fila = []  # Inicializa a fila como uma lista vazia

    def adicionar_cliente(self, nome):
        self.fila.append(nome)  # Adiciona o cliente ao final da fila
        print(f"Cliente {nome} adicionado à fila.")

    def atender_cliente(self):
        if not self.fila:
            print("Não há clientes na fila para atender.")
            return None
        cliente = self.fila.pop(0)  # Remove e retorna o cliente do início da fila
        print(f"Atendendo cliente: {cliente}")
        return cliente

    def tamanho_fila(self):
        tamanho = len(self.fila)  # Retorna o número de clientes restantes na fila
        print(f"Clientes na fila: {tamanho}")
        return tamanho

# Cria uma instância da fila de atendimento
fila = FilaAtendimento()

# Adiciona clientes à fila
fila.adicionar_cliente("Alice")
fila.adicionar_cliente("Bob")
fila.adicionar_cliente("Carlos")

# Exibe o tamanho da fila
fila.tamanho_fila()  # Deve exibir: Clientes na fila: 3

# Atende os clientes um por um
fila.atender_cliente()  # Deve exibir: Atendendo cliente: Alice
fila.atender_cliente()  # Deve exibir: Atendendo cliente: Bob

# Exibe o tamanho da fila novamente
fila.tamanho_fila()  # Deve exibir: Clientes na fila: 1
