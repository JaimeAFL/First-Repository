class persona:
    def __init__(self, nombre, apellido, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad

    def saludar(self):
        print("Hola, soy" + self.nombre + " " + self.apellido)

class italiano (persona):
    idioma_principal = "italiano"
    
    def __init__(self, nombre, apellido):
      self.nombre = nombre
      self.apellido = apellido
      self.nacionalidad = "italiana"

    def saludar(self):
        print ("¡Bonjorno! Mi nombre es: " + self.nombre + " " + self.apellido + 
                ", soy de nacionalidad " + self.nacionalidad + 
                " y mi idioma principal es " + self.idioma_principal + ".")

def crear_italiano (nombre, apellido):
    italiano_1 = italiano(nombre, apellido)
    return italiano_1

## PROGRAMA COMO TAL ##

nombre_usuario = input("Introduce tu nombre por favor: ")
apellido_usuario = input("Introduce tu apellido por favor: ")

personita = crear_italiano(nombre_usuario, apellido_usuario)
personita.saludar()
