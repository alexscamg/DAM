import csv
"""
# 1. % de ventas de cada vendedor
# 2. % sobre las ventas de cada cliente
# 3. 5 prod mas vendidos
# 4. Ingresos mensuales
"""

RUTA_BASE = '/Users/alejandrosanchezcaballero/Desktop/DAM/Programacion/Python_01/archivos/'
archivo = RUTA_BASE + 'cust_orders_prods.csv'

resultado = {}


def leer_archivo():
  contador = 0
  with open(archivo, 'r') as csv_file:
    lector = csv.DictReader(csv_file)
    for fila in lector:
      resultado[contador] = fila
      contador += 1

    print(resultado)

def por_ventas(resultado):
  total_vendedor = 0
  lista_cantidades = []
  lista_vendedores = []
  for n in resultado:       
    nombre_vendedor = resultado[n]['customer_name']  
    lista_vendedores.append(nombre_vendedor)
    for i in lista_vendedores:            # Iteramos el diccionario para sacar la info necesaria, hay que ver como ponerle los nombres automáticamente
      while i in resultado[n]["customer_name"]:
          lista_cantidades.append(int(resultado[n]["quantity"].replace('.', '')))
          break
    for cantidad in lista_cantidades:
      total_vendedor += cantidad

    

  print(lista_cantidades)
  print(lista_cantidades)





leer_archivo()
por_ventas(resultado)
