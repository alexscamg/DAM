import csv
import re

"""
# 1. % de ventas de cada vendedor
# 2. % sobre las ventas de cada cliente
# 3. 5 prod mas vendidos
# 4. Ingresos mensuales
"""

RUTA_BASE = '/Users/alejandrosanchezcaballero/Desktop/DAM/Programacion/Python_01/archivos/'
archivo = RUTA_BASE + 'cust_orders_prods-cust_orders_prods.csv'


def leer_archivo(archivo):
    resultado = {}
    contador = 0
    with open(archivo, 'r') as csv_file:
        lector = csv.DictReader(csv_file)
        for fila in lector:
            resultado[contador] = fila
            contador += 1
    return resultado


def total(datos):
    total = 0
    for elem in datos:
        cantidad = datos[elem]["quantity"].replace('.', '')
        total += int(cantidad)
    print(total)
    return total





def nombre_vendedores(resultado):
    vendedores_d = []
    for vendedores in resultado:
        vendedores_d.append(resultado[vendedores]["employee_name"])
    return vendedores_d





def porcentaje(resultado, lista, total):
    vendedores = {}
    vendedores_por = {}
    suma = 0
    for persona in lista:
        try:
            for indice in resultado:
                if persona == resultado[indice]["employee_name"]:
                    cantidad = resultado[indice]["quantity"]
                    suma += int(cantidad)
        finally:
            vendedores[persona] = suma
            suma = 0
    print(vendedores)
    for persona in lista:
        porcentaje = (vendedores[persona]*100)/total
        vendedores_por[persona] = porcentaje
    print(vendedores_por)


leer_archivo(archivo)
print()
# nombre_vendedores(leer_archivo(archivo))
print()
# total(leer_archivo(archivo))
print()


porcentaje(leer_archivo(archivo), nombre_vendedores(leer_archivo(archivo)), total(leer_archivo(archivo)))
