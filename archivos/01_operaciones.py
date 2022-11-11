"""
En python para abrir archivos con poner open ya nos abre el archivo
"""
# r, w, a, w+, r+, a+, b
archivo = open('/Users/alejandrosanchezcaballero/Desktop/DAM/Programacion/Python_01/archivos/pruebas.txt', 'r')
numeros = []

for linea in archivo:
  numeros.append(linea)



archivo.close()
print(numeros)
