ruta_base= '/home/alejandro/Proyectos/Python_01/archivos/'
tareas = ruta_base + 'tareas.txt'

def agenda():
  a = open(tareas, 'a+')
  lista_pen = []
  while True:
    pen = input('Dime qué tareas vas a hacer: ')
    if pen in lista_pen:
      print('Esa tarea está repetida')
    else:
      a.write(pen + '\n')
    if pen == '':
      break
  a.close()
  
def agenda2():
  a = open(tareas, 'a+')
  lista = []
  lineas = a.readlines()
  for linea in lineas:
    lista.append(linea)
  print(lista)

agenda()
agenda2()