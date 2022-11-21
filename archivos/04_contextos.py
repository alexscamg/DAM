RUTA_BASE = '/home/alejandro/Proyectos/Python_01/archivos/'
archivo = RUTA_BASE + 'datos_03.txt'

datos =  [
  {'nombre' :'Juan', 'apellido1':'Garcia', 'apellido2':'Romero', 'edad':22},
  {'nombre' :'Maria', 'apellido1':'López', 'apellido2':'Vega', 'edad':29},
  {'nombre' :'Miguel', 'apellido1':'Castillo', 'apellido2':'Garzón', 'edad':34},
]

with open(archivo, 'a+') as f: # NO tenemos que cerrarlo ya que se cierra solo
  for d in datos:
    cadena = d['nombre']+ ',' + d['apellido1']+ ',' + d['apellido2']+ ','+ str(d['edad']) + '\n'
    f.write(cadena)