"""
Contar la cantidad de palabras que hay en un archivo y escribirlo en el propio archivo     Alejandro Sanchez Caballero
"""

RUTA_BASE = '/home/alejandro/Proyectos/Python_01/Alejandro Sanchez Caballero Python/'
archivo = RUTA_BASE + 'archivo.txt'

def leer_reader(fichero):
  with open(fichero, 'r') as file:
    contenido_fichero = file.read()
    palabras_fichero = contenido_fichero.split()
    return len(palabras_fichero)


def escribir_archivo(fichero,valor):
  with open(fichero, 'a') as file:
    file.write(f"\nEl numero de palabras es: {valor} palabras")


escribir_archivo(archivo,leer_reader(archivo))










