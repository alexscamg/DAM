import csv
"""
# 1. % de ventas de cada vendedor
# 2. % sobre las ventas de cada cliente
# 3. 5 prod mas vendidos
# 4. Ingresos mensuales
"""

RUTA_BASE = '/home/alejandro/Proyectos/Python_01/archivos/'
archivo = RUTA_BASE + 'cust_orders_prods.csv'




def leer_archivo(archivo):
  resultado = {}
  contador = 0
  with open(archivo, 'r') as csv_file:
    lector = csv.DictReader(csv_file)
    for fila in lector:
      resultado[contador] = fila
      contador += 1
    print(resultado)
  return resultado

def total(datos):
  total = 0
  for elem in datos:
    cantidad = datos[elem]["quantity"].replace('.', '')
    total += int(cantidad)
  print(total)


print()


def nombre_vendedores(resultado):
  vendedores_d = {}
  for vendedores in resultado:
    vendedores_d[resultado[vendedores]["employee_name"]] = 0
  print(vendedores_d)
    
  
def por_ventas(resultado):
  vendedores_cantidad = {}
  for vendedores in resultado:    # Contador para sumar
    vendedores_cantidad[resultado[vendedores]["employee_name"]] = int(resultado[vendedores]["quantity"].replace('.', ''))
  
  print(vendedores_cantidad)



leer_archivo(archivo)
nombre_vendedores(leer_archivo(archivo))
total(leer_archivo(archivo))
por_ventas(leer_archivo(archivo))