clase_1 = [
  {"Alumno": "Alumno_1", "Latin": 8, "Castellano": 8, "Frances": 9, "Ingles": 4},
    {"Alumno": "Alumno_2", "Latin": 7, "Castellano": 6, "Frances": 7, "Ingles": 2},
    {"Alumno": "Alumno_3", "Latin": 10, "Castellano": 7, "Frances": 8, "Ingles": 9},
    {"Alumno": "Alumno_4", "Latin": 4, "Castellano": 4, "Frances": 3, "Ingles": 2},
    {"Alumno": "Alumno_5", "Latin": 9, "Castellano": 8, "Frances": 9, "Ingles": 6}
]

def suspensos_asignaturas(clase_1):
  asignaturas = ["Latin", "Castellano", "Frances", "Ingles"]
  umbral_suspenso = 5
  contador = {s: 0 for s in asignaturas}

  for alumno in clase_1:
    for s in asignaturas:
      if alumno[s] < umbral_suspenso:
        contador[s] = contador[s] + 1
  
  for s in asignaturas:
    print (s, "se ha suspendido por", contador [s], " alumnos")


def media_notas (clase_1):
  asignaturas = ["Latin", "Castellano", "Frances", "Ingles"] 
  for alumno in clase_1:
    suma = 0
    contador = 0

    for asignatura in asignaturas:
      suma = suma + alumno[asignatura]
      contador += 1
    
    media = suma / contador
    print (alumno ["Alumno"], "ha tenido una nota media de ", media)

def alumnos_aprobados(clase_1):
  asignaturas = ["Latin", "Castellano", "Frances", "Ingles"] 
  umbral_aprobado = 5
  aprobados = []
  
  for alumno in clase_1:
    suma = 0

    for asignatura in asignaturas:
      suma = suma + alumno [asignatura]

    media = suma /len(asignaturas)

    if media >= umbral_aprobado:
      aprobados.append(alumno["Alumno"])
  
  print("Los alumnos que han aprobado el curso son:", ", ".join(aprobados))


print("\n=== Suspensos por asignatura ===")
suspensos_asignaturas(clase_1)

print("\n=== Media de notas por alumno ===")
media_notas(clase_1)

print("\n=== Alumnos aprobados ===")
alumnos_aprobados(clase_1)
