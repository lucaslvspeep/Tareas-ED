filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = [["A" for _ in range(columnas)] for _ in range(filas)]
print("\nLa matriz resultante es: ")
for fila in matriz:
    print(fila)