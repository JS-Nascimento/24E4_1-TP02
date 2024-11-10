class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]  # Inicializa a tabela com listas vazias

    def _hash_funcao(self, chave):
        # Função de hash simples para calcular o índice
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash_funcao(chave)
        # Verifica se a chave já existe e atualiza o valor, se necessário
        for item in self.tabela[indice]:
            if item[0] == chave:
                item[1] = valor
                return
        # Se a chave não existir, adiciona a nova chave e valor
        self.tabela[indice].append([chave, valor])
        print(f"Chave '{chave}' com valor '{valor}' foi inserida na tabela.")

    def buscar(self, chave):
        indice = self._hash_funcao(chave)
        # Procura a chave na lista do índice calculado
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        # Retorna None se a chave não for encontrada
        print(f"Chave '{chave}' não encontrada.")
        return None

    def remover(self, chave):
        indice = self._hash_funcao(chave)
        for i, item in enumerate(self.tabela[indice]):
            if item[0] == chave:
                del self.tabela[indice][i]  # Remove o par (chave, valor)
                print(f"Chave '{chave}' foi removida da tabela.")
                return
        print(f"Chave '{chave}' não encontrada para remoção.")


# Cria uma tabela hash com tamanho 10
tabela = TabelaHash(10)

# Insere chaves e valores
tabela.inserir("nome", "Alice")
tabela.inserir("idade", 25)
tabela.inserir("cidade", "São Paulo")

# Busca valores
print(tabela.buscar("nome"))    # Deve exibir "Alice"
print(tabela.buscar("idade"))   # Deve exibir 25
print(tabela.buscar("cidade"))  # Deve exibir "São Paulo"
print(tabela.buscar("pais"))    # Deve exibir "Chave 'pais' não encontrada."

# Remove uma chave
tabela.remover("idade")
print(tabela.buscar("idade"))   # Deve exibir "Chave 'idade' não encontrada."
