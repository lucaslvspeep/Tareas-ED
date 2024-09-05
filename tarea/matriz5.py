matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        num = float(input(f"Ingresa el elemento [{i+1},[{i+1}]: ]"))
        fila.append(num)
        matriz.append(fila)
diagonal_principal = [matriz[i][i] for i in range(3)]
print(f"Elementos de la diagonal principal: ")
print(diagonal_principal)