def limpiar (fila): #Funcion para limpiar filas de comillas, espacios en blanco y saltos de linea
    salida = [] #Lista vacias donde meteremos el resultado de la funcion
    for elem in fila:
        elem = elem.replace('"', '').strip()
        elem = elem.replace('\n', '')
        salida.append(elem)
    
    return salida



ruta_base = '/home/alejandro/Proyectos/Python_01/archivos/'
datos = ruta_base + 'hurricanes.csv'
huracanes = []

archivo = open(datos,'r')
cabeceras = archivo.readline()
claves = limpiar(cabeceras.split(","))

for linea in archivo:
    fila = limpiar(linea.split(","))
    d = {}
    for i in range (len(fila)):
        d[claves[i]] = fila [i]
    huracanes.append(d)

import pprint

pprint.pprint(huracanes)

