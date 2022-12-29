"""
Almacenar en un diccionario los nombres de los meses del año y sus respectivos numeros de orden. La funcion debe decir el numero al darle el nombre del mes   Alejandro Sanchez Caballero
"""
def numero_mes(nombre_mes):
  meses= {
      'Enero' : 1,
      'Febrero': 2,
      'Marzo' : 3,
      'Abril' : 4,
      'Mayo' : 5,
      'Junio' : 6,
      'Julio' : 7,
      'Agosto' : 8,
      'Septiembre' : 9,
      'Octubre': 10,
      'Noviembre': 11,
      'Diciembre' : 12
  }
  try:
    return f'El mes {nombre_mes.capitalize()} es el mes numero {meses[nombre_mes.capitalize()]} del año'
  except:
    return f'El mes {nombre_mes.capitalize()} no es un mes'


mes = input('Introduce el mes del que desa saber su numero de orden: ')
print(numero_mes(mes))