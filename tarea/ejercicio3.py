numeros = []

for i in range(7):
    num = float(input(f"Ingresa el número {i+1}: "))
    numeros.append(num)

if numeros:
    mayor = numeros[0]

    for num in numeros:
        if num > mayor:
            mayor = num

    print(f"El número mayor es: {mayor}")
else:
    print("La lista está vacía.")
