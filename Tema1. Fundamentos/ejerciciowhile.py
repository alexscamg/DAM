# de una lista de palabras
# encontrar la mas larga e imprimirla

palabras = ['hola', 'adios', 'manzana', 'pera', 'pin']

indice_max = -1
max_len = 0

for i in range(len(palabras)):
  largo = len(palabras[i])
  if largo > max_len:
    indice_max = i
    max_len = largo

print(palabras[indice_max])