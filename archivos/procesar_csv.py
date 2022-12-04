import csv
import pprint
import os
from heapq import nlargest

"""
# 1. % de ventas de cada vendedor
# 2. % sobre las ventas de cada cliente
# 3. 5 prod mas vendidos
# 4. Ingresos mensuales
"""

RUTA_BASE = '/Users/alejandrosanchezcaballero/Desktop/DAM/Programacion/Python_01/archivos/'
archivo = RUTA_BASE + 'cust_orders_prods-cust_orders_prods.csv'


def leer_archivo(archivo):              # Leer el archivo para procesar los datos
    resultado = {}
    contador = 0
    with open(archivo, 'r') as csv_file:
        lector = csv.DictReader(csv_file)
        for fila in lector:
            resultado[contador] = fila
            contador += 1
    return resultado


def total(datos):                     # Calcula el total de las cantidades
    total = 0
    for elem in datos:
        cantidad = datos[elem]["quantity"].replace('.', '')
        total += int(cantidad)
    return total


def nombre_vendedores(resultado):           # Guarda el nombre de los vendedores en una lista
    vendedores_d = []
    for vendedores in resultado:
        vendedores_d.append(resultado[vendedores]["employee_name"])
    return vendedores_d

def nombre_clientes(resultado):           # Guarda el nombre de los vendedores en una lista
    clientes_d = []
    for clientes in resultado:
        clientes_d.append(resultado[clientes]["customer_name"])
    return clientes_d

def nombre_productos(resultado):         # Guarda el nombre de los productos en una lista
    productos_d = []
    for productos in resultado:
        productos_d.append(resultado[productos]["product_name"])
    return productos_d

def porcentaje_ventas(resultado, lista, total):           # Calcula el porcentaje de las ventas
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
    for persona in lista:
        porcentaje = (vendedores[persona]*100)/total
        vendedores_por[persona] = str(round(porcentaje, 2))+'%'
    pprint.pprint(vendedores_por)


def porcentaje_clientes(resultado, lista, total):                # Calcula el porcentaje de la ventas de los clientes
    clientes = {}
    clientes_por = {}
    suma = 0
    for persona in lista:
        try:
            for indice in resultado:
                if persona == resultado[indice]["customer_name"]:
                    cantidad = resultado[indice]["quantity"]
                    suma += int(cantidad)
        finally:
            clientes[persona] = suma
            suma = 0

    for persona in lista:
        porcentaje = (clientes[persona]*100)/total
        clientes_por[persona] = str(round(porcentaje, 2))+'%'
    pprint.pprint(clientes_por)

def product(resultado, lista):                       # Calcula las cantidades de productos que hay, 
                                                    #  ¡¡¡¡Falta hacer que saque los 5 que mas se han vendido!!!!
    nombre_productos = {}
    productos_cant = {}
    mas_5 = {}
    suma = 0
    for producto in lista:
        try:
            for indice in resultado:
                if producto == resultado[indice]["product_name"]:
                    cantidad = resultado[indice]["quantity"]
                    suma += int(cantidad)
        finally:
            nombre_productos[producto] = suma
            suma = 0
    productos_mas_vendidos = nlargest(5, nombre_productos, key=nombre_productos.get)
    pprint.pprint(f'Los 5 productos mas vendidos son: {productos_mas_vendidos}')
    
    

def facturacion(resultado):             # Saca la facturación por mes
    dict_meses = {"01": 0,"02": 0,"03": 0,"04": 0,"05": 0,"06": 0,"07": 0,"08": 0,"09": 0,"10": 0,"11": 0,"12": 0}
    for n in resultado:
        for mes in dict_meses:
            if resultado[n]["order_date"][5:7] in mes:
                dict_meses[mes] += int(resultado[n]["quantity"].replace(',','')) * int(resultado[n]["unit_price"].replace(',',''))
    pprint.pprint(dict_meses)


def pinta_menu():           # Pinta el menu
    print('------MENU------- ')
    print('1. % de ventas de cada vendedor')
    print('2. % sobre las ventas de cada cliente')
    print('3. 5 prod mas vendidos')
    print('4. Ingresos mensuales')
    print('5. Salir')


def limpia_pantalla():
    os.system('clear')

def main():
    limpia_pantalla()
    pinta_menu()
    datos = leer_archivo(archivo)
    while True: 
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            limpia_pantalla()
            porcentaje_ventas(datos, nombre_vendedores(datos), total(datos))
            pinta_menu()
        if opcion == 2:
            limpia_pantalla()
            porcentaje_clientes(datos, nombre_clientes(datos), total(datos))
            pinta_menu()
        if opcion == 3:
            limpia_pantalla()
            product(datos,  nombre_productos(datos))
            pinta_menu()
        if opcion == 4:
            limpia_pantalla()
            facturacion(datos)
            pinta_menu()
        if opcion == 5:
            exit()



main()


