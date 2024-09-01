temperaturas = []
print("Por favor, ingresa 10 temperaturas")

for i in range(10):

    temperatura = float(input(f"temperatura {i + 1}: "))
    temperaturas.append(temperatura)

promedio = sum(temperaturas) / len(temperaturas)

print(f"\nEl promedio de las temperaturas es: {promedio:.2f}")

while True:
    opcion = input("\n¿Ver alguna tempertura especifica? (sí/no)").strip().lower()

    if opcion == "sí":
        posicion = int(input("Ingresa la posición (1-10) de la temperatura que deseas ver: "))
        if 1 <= posicion <= 10:
            print(f"La temperatura en la posición {posicion} es: {temperaturas[posicion - 1]:.2f}")
        else:
            print("Posición fuera de rango. Por favor, ingresa un número entre 1 y 10.")

    elif opcion == "no":
        print("Cierre el programa.")
        break
    else:
        print("Por favor, ingrese 'sí' o 'no'.")