# -*- coding: utf-8 -*-
"""
Ejemplo de módulo ejecutable
"""

# Definición de funciones

def llama_a_la_puerta_de(persona, n_veces=3):
    """Llama a la puerta de la persona las veces que haga falta"""
    return [ "Toc,toc,toc! " + persona + "!" for i in range(n_veces) ]


# Cuerpo principal ejecutable

# si estamos dentro del namespace __main__
if __name__ == "__main__":
    # ejecuta cosas!!
    print("Ejecutamos el main")
    print(llama_a_la_puerta_de("Penny"))
    