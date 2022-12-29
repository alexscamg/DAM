import pprint

"""
Solicitar un nombre al usuario y su precio y luego mostrarlo como listado  Alejandro Sanchez Caballero
"""

def articulos():
  listado_articulos = {}
  while True:
      articulo = input('Introduce un articulo: ')
      if articulo == '':
          break
      else:
        precio = input('Introduce su precio: ')
        try:
            articulo = str(articulo) 
            precio = float(precio)
        except:
            print('El articulo no se a podido introducir porque no tiene un precio valido') 
            continue
        else:
          listado_articulos[articulo] = str(precio) + '€'
  return listado_articulos




pprint.pprint(articulos())