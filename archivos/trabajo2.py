ruta_base= '/home/alejandro/Proyectos/Python_01/archivos/'
tareas = ruta_base + 'tareas.txt'

def agenda():
  a = open(tareas, 'a+')
  lista_pen = []
  lista_ter = []
  while True:
    pen = input('Dime qué tareas vas a hacer: ')
    if pen in lista_pen:
      print('Esa tarea está repetida')
    else:
      lista_pen.append(pen)
    if pen == '':
      break
  while True:
    ter = input('Dime qué tareas has terminado: ')
    if ter == '':
      break
    if ter in lista_ter:
      print('Esa tarea ya está terminada')
    if ter in lista_pen:
      lista_pen.remove(ter)
      lista_ter.append(ter)
    else:
      lista_ter.append(ter)
  lista_pen.pop()
  a.write('La lista de tareas pendientes es: ' + str(lista_pen) + '\n')
  a.write('La lista de tareas terminadas es: ' + str(lista_ter) + '\n')
  a.close()

agenda()













