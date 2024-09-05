numeros = []
for i in range(8):
    num = float(input(f"Ingresa el número {i+1}: "))
    numeros.append(num)
positivos = sum(1 for num in numeros if num > 0)
print(f"Cantidad de números positivos: {positivos}")