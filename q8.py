def inverter_fila(fila):
    fila.reverse()  # Inverte a ordem da fila in-place
    return fila

def inverter_fila(fila):
    return fila[::-1]  # Retorna uma nova lista com a ordem invertida

# Exemplo de fila de pacientes em ordem de chegada
fila_pacientes = ["Paciente 1", "Paciente 2", "Paciente 3", "Paciente 4"]

# Invertendo a fila
fila_invertida = inverter_fila(fila_pacientes)
print("Fila invertida:", fila_invertida)


fila_invertida: ["Paciente 4", "Paciente 3", "Paciente 2", "Paciente 1"]

# Invertendo a fila
fila_invertida = inverter_fila(fila_pacientes)
print("Fila invertida:", fila_invertida)
