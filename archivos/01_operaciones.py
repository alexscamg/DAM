"""
En python para abrir archivos con poner open ya nos abre el archivo
"""
# r, w, a, 
# w+(si existe se borra, si no se crea)
# r+ (si no existe da error)
# a+(si existe se añade por el final)
# b
archivo = open('/Users/alejandrosanchezcaballero/Desktop/DAM/Programacion/Python_01/archivos/pruebas.txt', 'r')
numeros = []

for linea in archivo:
  numeros.append(linea)



archivo.close()
print(numeros)
