''' 
- Insertar tareas
- Leer tareas
- Mostrar estados
- Modificar estados
- Borrar tareas


tareas_pendientes = []

'''



ruta_base= '/home/alejandro/Proyectos/Python_01/archivos/'
pendientes = ruta_base + 'tareaspendientes.txt'
hechos = ruta_base + 'tareasterminadas.txt'






























""" def t_pendientes (): 
  tareas_pendientes = []
  while True:

    tarea = input('introduce la tarea a realizar: ')
    tareas_pendientes.append(tarea)
  
    if tarea == '':
      break
  tareas_pendientes.pop()
  return tareas_pendientes



def t_terminadas ():
  tareas_hechas = []
  while True:
    tarea_hecha = input('Dime qué tareas has terminado: ')
    if tarea_hecha in t_pendientes:
      tareas_hechas.append(tarea_hecha) 
      t_pendientes.remove(tarea_hecha)
    else:
      break
  return tareas_hechas


t_pendientes()

t_terminadas()



 """