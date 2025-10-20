# -------------------------------------
# Herencia de clase Persona -> Italiano
# -------------------------------------
# Objetivo:
# - persona: modelo base con nombre, apellido y nacionalidad.
# - italiano: subclase que fija nacionalidad e idioma y redefine saludar().
# - crear_italiano(): funcion para crear una persona italiana.
# - Bloque principal: pide datos por consola y saluda.

class persona:
    def __init__(self, nombre, apellido, nacionalidad):
        # Estado común a cualquier persona
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad

    def saludar(self):
        # Cuando se llama, muestra en la terminal saludo
        print("Hola, soy" + self.nombre + " " + self.apellido)

class italiano(persona):
    # Atributo de clase: igual para todas las personas italianas
    idioma_principal = "italiano"
    
    def __init__(self, nombre, apellido):
        # Toma de herencia la clase 'persona' y se cambia
        # el valor de nacionalidad por uno concreto
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = "italiana"

    def saludar(self):
        # Sobrescritura del método: saludo específico con idioma y nacionalidad
        print("¡Bonjorno! Mi nombre es: " + self.nombre + " " + self.apellido +
            ", soy de nacionalidad " + self.nacionalidad +
            " y mi idioma principal es " + self.idioma_principal + ".")

def crear_italiano(nombre, apellido):
    # Función que encapsula la creación de un italiano
    italiano_1 = italiano(nombre, apellido)
    return italiano_1

# Entrada de usuario y concatenación de acciones
nombre_usuario = input("Introduce tu nombre por favor: ")
apellido_usuario = input("Introduce tu apellido por favor: ")

# Crea una instancia de italiano y ejecuta su comportamiento específico
personita = crear_italiano(nombre_usuario, apellido_usuario)
personita.saludar()