matriz = []
for i in range(2):
    fila = []
    for j in range(3):
        num = float(input(f"Ingresa el elemento [{i+1},{j+1}]: "))
        fila.append(num)
        matriz.append(fila)
transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print("Matriz transpuesta: ")
for fila in transpuesta:
    print(fila)