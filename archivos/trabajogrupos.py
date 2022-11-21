''' 
- Insertar tareas
- Leer tareas
- Mostrar estados
- Modificar estados
- Borrar tareas


tareas_pendientes = []




'''
tareas_hechas = []
tareas_pendientes = []
tpd = {}
thd = {}
ruta_base= '/home/alejandro/Proyectos/Python_01/archivos/'
pendientes = ruta_base + 'pendientes.txt'
hechos = ruta_base + 'hechos.txt'
def dime_tarea (): 
  while True:

    tarea = input('introduce la tarea a realizar: ')
    tareas_pendientes.append(tarea)
  
    if tarea == '':
      break



def id_pen(*tareas_pendientes):
  
  for t in range(len(tareas_pendientes)):
    tpd[t] = tareas_pendientes[t]
  
  return tpd



def lista_h():
  while True:
    tarea_hecha = input('Dime qué tareas has terminado: ')
    if tarea_hecha in tareas_pendientes:
      tareas_hechas.append(tarea_hecha) 
      tareas_pendientes.remove(tarea_hecha)
    else:
      break







dime_tarea()
tareas_pendientes.pop()
id_pen()
lista_h()

print(tareas_pendientes)
print(id_pen(*tareas_pendientes))
print(tareas_hechas)

'''  
  tareas = input('Dime qué tareas tienes: ')
'''