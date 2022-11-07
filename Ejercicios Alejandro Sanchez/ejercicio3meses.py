"""La duración de un mes varía de 28 a 31 días. 

En este ejercicio, creará un programa que lea el nombre de un mes del usuario como una cadena. 

Entonces su programa debería mostrar el número de días en ese mes. 

Muestre "28 o 29 días" para febrero para que se aborden los años bisiestos."""

# Definimos la función
def diasmeses(mes):
  meses = {
      'enero' : '31',
      'febrero': '28 0 29',
      'marzo' : '31',
      'abril' : '30',
      'mayo' : '31',
      'junio' : '30',
      'julio' : '31',
      'agosto' : '31',
      'septiembre' : '30',
      'octubre': '31',
      'noviembre': '30',
      'diciembre' : '31'
      
      }
  # Pasamos el mes del usuario a minusculas y lo hacemos una variable
  diasmes = meses[mes.lower()]
  # Retornamos el valor del 
  return f'El mes {mes} tiene {diasmes} dias'


mes = input('Introduce un mes para ver sus dias: ')
print(diasmeses(mes))