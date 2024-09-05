print("ingresa los elementos de la primera matriz 2x2:")
matriz1 = [[float(input(f"elemento [{i+1},{j+1}]: ")) for j in range(2)] for i in range(2)]

print("ingresa los elementos de la segunda matriz 2x2:")
matriz2 = [[float(input(f"elemento [{i+1},{j+1}]: ")) for j in range(2)] for i in range(2)]

resultado = [[sum(matriz1[i][k] * matriz2[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

print("Resultado de la multiplicación: ")
for fila in resultado:
    print(fila)