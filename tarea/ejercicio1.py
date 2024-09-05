vector = []
for i in range(5):
    num = float(input(f"Ingresa el número {i+1}: "))
    vector.append(num)
suma = sum(vector)
print(f"La suma de los elementos es: {suma}")