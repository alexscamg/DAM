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
    vendedores_d = []
    for vendedores in resultado:
        vendedores_d.append(resultado[vendedores]["employee_name"])
    return vendedores_d


print()


def porcentaje(resultado, lista):
    vendedores = {}
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


def por_ventas(resultado):
    vendedores_cantidad = {}
    for vendedores in resultado:    # Contador para sumar
        vendedores_cantidad[resultado[vendedores]["employee_name"]] = int(
            resultado[vendedores]["quantity"].replace('.', ''))

    print(vendedores_cantidad)


leer_archivo(archivo)
# nombre_vendedores(leer_archivo(archivo))
# total(leer_archivo(archivo))
# por_ventas(leer_archivo(archivo))

porcentaje(leer_archivo(archivo), nombre_vendedores(leer_archivo(archivo)))
