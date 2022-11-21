RUTA_BASE = '/home/alejandro/Proyectos/Python_01/archivos/'
archivo = RUTA_BASE + 'datos_03.txt'

datos =  [
  {'nombre' :'Juan', 'apellido1':'Garcia', 'apellido2':'Romero', 'edad':22},
  {'nombre' :'Maria', 'apellido1':'López', 'apellido2':'Vega', 'edad':29},
  {'nombre' :'Miguel', 'apellido1':'Castillo', 'apellido2':'Garzón', 'edad':34},
]
f = open(archivo, 'w')

for d in datos:
  cadena = d['nombre']+ ',' + d['apellido1']+ ',' + d['apellido2']+ ','+ str(d['edad']) + '\n'
  f.write(cadena)

f.close()


"""
escribe_archivo(nombre, datos)
"""

def escribe_archivo(nombre_archivo, datos):
  f = open(nombre_archivo, 'a+')
  f.write(datos)
  f.close()

mi_arch = RUTA_BASE + 'mi_arch.txt'
c1 = "Juan Garcia Romero, 24\n"
c2= "Maria Lopez Sanchez, 26\n"
c3 ="Perico, Periquita, 35\n"
escribe_archivo(mi_arch, c1)
escribe_archivo(mi_arch, c2)
escribe_archivo(mi_arch, c3)