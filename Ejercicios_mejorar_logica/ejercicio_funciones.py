
palabra = "HOLA"

for i in range (10):
    if len(palabra) - 1 < 10:
        palabra += "X"

print(palabra)
print ("El tamaño de palabra es: ", len(palabra))
print("La ultima posicion es: ", len(palabra)-1)