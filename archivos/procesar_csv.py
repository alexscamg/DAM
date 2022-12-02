import csv

"""
# 1. % de ventas de cada vendedor
# 2. % sobre las ventas de cada cliente
# 3. 5 prod mas vendidos
# 4. Ingresos mensuales
"""

RUTA_BASE = '/home/alejandro/Proyectos/Python_01/archivos/'
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

def nombre_clientes(resultado):
    clientes_d = []
    for clientes in resultado:
        clientes_d.append(resultado[clientes]["customer_name"])
    return clientes_d

def nombre_productos(resultado):
    productos_d = []
    for productos in resultado:
        productos_d.append(resultado[productos]["product_name"])
    return productos_d

def porcentaje_ventas(resultado, lista, total):
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
        vendedores_por[persona] = str(round(porcentaje, 2))+'%'
    print(vendedores_por)


def porcentaje_clientes(resultado, lista, total):
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
    print(clientes)
    for persona in lista:
        porcentaje = (clientes[persona]*100)/total
        clientes_por[persona] = str(round(porcentaje, 2))+'%'
    print(clientes_por)

def product(resultado, lista):
    nombre_productos = {}
    productos_cant = {}
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
    print(nombre_productos)
    
    

def facturacion(resultado):
  dict_meses = {"01": 0,"02": 0,"03": 0,"04": 0,"05": 0,"06": 0,"07": 0,"08": 0,"09": 0,"10": 0,"11": 0,"12": 0}
  for n in resultado:
      for mes in dict_meses:
          if resultado[n]["order_date"][5:7] in mes:
              dict_meses[mes] += int(resultado[n]["quantity"].replace(',','')) * int(resultado[n]["unit_price"].replace(',',''))
  print(dict_meses)





def menu():
  print('MENU: ')
  print('1. % de ventas de cada vendedor')
  print('2. % sobre las ventas de cada cliente')
  print('3. 5 prod mas vendidos')
  print('4. Ingresos mensuales')




leer_archivo(archivo)
print()
# nombre_vendedores(leer_archivo(archivo))
print()
# total(leer_archivo(archivo))
print()


porcentaje_ventas(leer_archivo(archivo), nombre_vendedores(leer_archivo(archivo)), total(leer_archivo(archivo)))
print()

porcentaje_clientes(leer_archivo(archivo), nombre_clientes(leer_archivo(archivo)), total(leer_archivo(archivo)))

print()
product(leer_archivo(archivo), nombre_productos(leer_archivo(archivo)))
print()

facturacion(leer_archivo(archivo))


