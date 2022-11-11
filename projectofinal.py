import string
import pprint
"""
1.  Pasar a minusculas
1b. Quitar los signos de puntuación
2.  ignorar palabras de 3 letras o menos
3.  Dividir la cadena por palabras
4.  Procesar la cadena
"""

def frecuencias(texto):
  diccionario = {}
  # 1.
  texto = texto.lower()
  # 1b. 
  puntuacion = string.punctuation
  for p in puntuacion:
    texto = texto.replace(p, '')
  palabras = texto.split()
  for i in palabras:
    if len(i) > 3:
      if diccionario.get(i) == None:
        diccionario[i] = 1
      else:
        diccionario[i] +=1


  return(diccionario)


texto = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas 'Letraset', las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum."

pprint.pprint(frecuencias(texto))
