tamaño = 4
matriz_identidad = [[1 if i == j else 0 for j in range(tamaño) for i in range(tamaño)]]
print("Matriz identidad de tamaño 4x4: ")
for fila in matriz_identidad:
    print(fila)