vector = []
for i in range(6):
    num = float(input(f"Ingresa el número {i+1}: "))
    vector.append(num)
vector_invertido = vector[::-1]
print(f"El vector invertido es: {vector_invertido}")