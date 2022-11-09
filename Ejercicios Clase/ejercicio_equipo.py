import random
import pprint
"""
Tenemos un conjunto de personas, creamos una funcion para hacer equipos con la gente que nos indique y devuelva una lista de lista
"""
alumnos = ['Javi', 
'Jose',
'Miguel', 
'A.Muñoz', 
'Ana', 
'A.Sánchez', 
'Luciano', 
'Juan', 
'Pablo', 
'Dani', 
'Pedro',
'P.Gonzalez',
'Carlos',
'Adrián']

# 1. Calcular el numero de equipos
# 2. Crear las listas y llenarlas ALEATORIAMENTE sin que se repitan
# 3. 
print()

def crea_equipos(gente,miembros):
  if len(gente) < miembros:
    return gente
  if miembros == 0:
    return []
  num_equipos = len(gente)//miembros
  salida = []
  offset = 0
  random.shuffle(gente)
  for i in range(num_equipos):
    salida.append([gente[offset], gente[offset+1]])
    offset +=2
  return salida


print(crea_equipos(alumnos,2))
print()

def migue(gente, miembros):
  random.shuffle(gente)
  num_grupos = len(gente)//miembros

  listas= []
  for i in range(num_grupos):
    equipo = []
    for j in range(miembros):
      equipo.append(gente.pop())
    listas.append(equipo)


  for p in range(len(gente)):
    listas[p].append(gente[p])

  return listas


pprint.pprint(migue(alumnos,3))
  
