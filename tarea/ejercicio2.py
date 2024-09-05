numeros = []
for i in range(10):
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)
promedio = sum(numeros) / len(numeros)
print(f"El promedio de los valores ingresados es: {promedio}")