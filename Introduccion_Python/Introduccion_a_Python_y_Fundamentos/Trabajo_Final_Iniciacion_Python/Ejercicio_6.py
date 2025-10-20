# --------------
# Agenda simple: 
# --------------
# Crea clave "nombre apellidos" y guardar teléfono

# Normaliza nombre y apellidos: quita espacios, pasa a minúsculas y construye la clave.
def clave_contacto(nombre, apellidos):
    nom = str(nombre).strip().lower()
    ape = str(apellidos).strip().lower()
    return f"{nom} {ape}"

# Pide un teléfono hasta que sea válido: exactamente 9 dígitos.
def numero_telefono():
    while True:
        telefono = input(" Por favor, introduzca el número de telefono: ").strip()
        if len(telefono) == 9 and telefono.isdigit():
            return telefono
        print("Por favor, introduzcta un numero de teléfono válido")

# Pregunta sí/no y devuelve True/False. Reintenta para otras respuestas.
def preguntar_si_no(respuesta):
    while True:
        pregunta = input(respuesta).strip().lower()
        if pregunta == "si":
            return True
        if pregunta == "no":
            return False
        print("responda SI o NO")

# Diccionario de la agenda: clave -> teléfono.
agenda = {}

# Bucle principal:
# 1) Pide nombre y apellidos.
# 2) Construye la clave normalizada.
# 3) Evita duplicados.
# 4) Pide teléfono validado.
# 5) Pregunta si desea añadir otro. Si no, muestra la agenda y termina.
while True:
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    clave = clave_contacto(nombre, apellidos)

    # Control de duplicados: no sobrescribir contactos existentes.
    if clave in agenda:
        print("Ese contacto ya existe. Pruebe con otro diferente")
        continue

    # Teléfono validado y alta en la agenda.
    telefono = numero_telefono()
    agenda[clave] = telefono

    # Decisión de continuar o finalizar. Si finaliza, imprime el resumen.
    if not preguntar_si_no("¿Añadir otro? (SI/NO): "):
        print("Agenda:")
        for clave in agenda:
            print(f"- {clave}: {agenda[clave]}")
        break
