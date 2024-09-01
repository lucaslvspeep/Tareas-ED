Datos_Basicos = {"Nombres": "Juan Carlos",
                 "Apellidos": "Pérez García",
                 "DUI": "01025487-9",
                 "Fecha_nacimiento": "23/07/1980",
                 "Lugar_Nacimiento": "Soya city",
                 "Nacionalidad": "Salvadoreña",
                 "Estado_Civil": "Complicado"}

print("\nDetalle del diccionario")
print("==========================")

print("\nClaves del diccionario: ",Datos_Basicos.keys())
print("\nValores del diccionario; ",Datos_Basicos.values())
print("\nElementos del diccionario: ",Datos_Basicos.items)

print("\nInscripción del curso")
print("=========================")

print("\nDatos del participante")
print("==========================")

print("DUI:",Datos_Basicos["DUI"])
print("Nombre completo: ",Datos_Basicos["Nombres"]+" "+Datos_Basicos["Apellidos"])