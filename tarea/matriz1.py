matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        num = float(input(f"Ingresa el elemento [{i+1},{j+1}]: "))
        fila.append(num)
        matriz.append(fila)
    suma = sum(sum(fila) for fila in matriz)
print(f"la suma de todos los elementos es: {suma}")