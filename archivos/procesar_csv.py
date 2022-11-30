import csv

"""
1. % de ventas de cada vendedor
2. % sobre las ventas de cada cliente
3. 5 prod mas vendidos
4. Ingresos mensuales
"""



RUTA_BASE = '/home/alejandro/Proyectos/Python_01/archivos/'
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
  total_cantidad = 0
  total_vendedor = 0
  for elem in resultado:                #accedemos a cada elemento de la lista (en este caso cada elemento es un diccionario)
    cantidad = elem['quantity']
    x = cantidad.replace('.', '')
    total_cantidad += int(x)
  print(total_cantidad)

  
  for elem in resultado:
    
    vendedor = elem['employee_name']
    total_vendedor = 0
    cantidad_vendedor = elem['quantity']
    x = cantidad_vendedor.replace('.', '')
    total_vendedor += int(x)
    print(f'{vendedor} ha vendido {total_vendedor}')







leer_archivo()
por_ventas(resultado)
