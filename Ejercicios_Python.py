# 1. Slice con paso negativo
# Invierte la cadena "anaconda" en una sola línea usando slicing:

palabra = "anaconda"

inversa = palabra[::-1]   
print(inversa)
s = "abcdef"
print(s[2:5])

# ejercicio 2 (diccionario + get con valor por defecto):

capitales = {"España": "Madrid", "Francia": "París"}
print(capitales.get("Italia", "Desconocida"))

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
comunes = (set1 & set2)        # ← completa aquí con el operador adecuado
print(comunes)     # → {3, 4}

ratio = 0.873 ; print(f"Éxito: {ratio:,.1%}".replace(".",",").replace("%"," %"))

ratio = 0.125 ; print(f"{ratio:.2%}")

ratio = 0.873
print(f"Éxito: {ratio:.1%}".replace('.', ',').replace('%', ' %'))

# 5 — comprensión de lista con condición
# Crea pares_cuadrados con los cuadrados de los números pares del 0 al 9:

pares_cuadrados = [x**2 for x in range (10) if x % 2 == 0]   # → [0, 4, 16, 36, 64]
print(pares_cuadrados)

# 6 — desempaquetado múltiple (ignorar con _)
# Completa y ejecuta:

def trio():
    return 1, 2, 3

primero, segundo, ultimo = trio()
print(primero, ultimo) 

# 7 — enumerate()
# Completa y ejecuta para ver “0 → a”, “1 → b”, “2 → c”:

letras = ["a", "b", "c"]
for indice, letra in enumerate(letras):
    print(f"{indice} → {letra}")

# 8 — join()
# Completa y ejecuta:

colores = ["rojo", "verde", "azul"]
resultado = ", ".join(colores)
print(resultado)

#9 — función con *args

#Define maximo(*args) que:
#si no recibe números → devuelva None
#si recibe números → devuelva el mayor
#Pista breve: comprueba primero si args está vacío y, si no, usa el mayor de args.



def maximo(*n):
    if not n:
        return None
    return max(n)

print(maximo(3, 7, 2))   # → 7
print(maximo())

def f(*args): print(args)
f(10, *[20, 30])

#10 — all():
nums = [2, 3, 6, 8]
hay_impar = any(n % 2 != 0 for n in nums)
todos_pares = all(n % 2 == 0 for n in nums)
print(todos_pares)
print(hay_impar)

# 1) Paréntesis (precedencia)
resultado = 2 + 3 * 4
# toca los paréntesis
print(resultado)  # → 20

resultado = (2 + 3) * 4
print(resultado)

nums = [10, 20, 30, 40, 50, 60]
ultimos = nums[-3:]
print(ultimos)

s = "ABCDEFGH"
impares = s[1::2]
print(impares)

persona = {"nombre": "Ana", "edad":"30"}
# añade clave "edad" con valor 30
print(persona["edad"])  # → 30

a = {1, 2, 3, 4}
b = {3, 4, 5}
solo_a =  a ^ b       # ← aquí
print(solo_a)    # → {1, 2}

pal = "hola"
print(f">>>{pal:^7}<<<")

print(round(2/3, 2))

print("hello world")


def suma_digitos(n):
    suma = 0 
    while n > 0:
        digito = n % 10
        suma += digito
        n //= 10
    return suma

def es_capicua(n):
    s = str(n)
    return s == s[::-1]

def es_capicua(n):
    original = n
    invertido = 0
    while n > 0:
        invertido = invertido * 10 + (n % 10)
        n //= 10
    return original == invertido

for i in range (1,1000000):
    if i % 3 == 0 and i % 7 == 0 and suma_digitos(i) == 18 and es_capicua(i):
        print(i)


numbers = filter(lambda x: x % 2 != 0, [1,2,3,4,5])
print(list(numbers))
