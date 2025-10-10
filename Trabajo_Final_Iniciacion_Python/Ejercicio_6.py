def clave_contacto (nombre, apellidos):
    nom = str(nombre).strip().lower()
    ape = str(apellidos).strip().lower()
    return f"{nom} {ape}"

def numero_telefono ():
    while True:
        telefono = input(" Por favor, introduzca el número de telefono: ").strip()
        if len(telefono) == 9 and telefono.isdigit(): return telefono
        print("Por favor, introduzcta un numero de teléfono válido")

def preguntar_si_no(respuesta):
    while True:
        pregunta = input(respuesta).strip().lower()
        if pregunta == "si": return True
        if pregunta == "no": return False
        print("responda SI o NO")

## AGENDA ##

agenda = {}

while True: 
    nombre = input("Nombre: ") 
    apellidos = input("Apellidos: ") 
    clave = clave_contacto(nombre,apellidos)

    if clave in agenda:
        print("Ese contacto ya existe. Pruebe con otro diferente")
        continue

    telefono = numero_telefono()
    agenda[clave] = telefono

    if not preguntar_si_no("¿Añadir otro? (SI/NO): "):
        print("Agenda:")
        for clave in agenda:
            print(f"- {clave}: {agenda[clave]}")
        break
