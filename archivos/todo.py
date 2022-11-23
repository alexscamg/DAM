''' 
- Insertar tareas
- Leer tareas
- Mostrar estados
- Modificar estados
- Borrar tareas
'''
RUTA_BASE = '/Users/alejandrosanchezcaballero/Desktop/DAM/Programacion/Python_01'
archivo = RUTA_BASE + 'todo.txt'

tareas = {}

def new_tarea():
  
  tarea = input('Introduce una tarea: ')
  estado = input('Define el estado de la tarea: ')

  f = open(archivo, 'w+')

  tareas[tarea] = estado
  for d in tareas:
    cadena = d[tarea]+'\n'
  f.write(cadena)

  f.close()


new_tarea()

