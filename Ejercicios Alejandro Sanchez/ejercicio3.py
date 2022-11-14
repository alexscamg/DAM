"""La duración de un mes varía de 28 a 31 días. 

En este ejercicio, creará un programa que lea el nombre de un mes del usuario como una cadena. 

Entonces su programa debería mostrar el número de días en ese mes. 

Muestre "28 o 29 días" para febrero para que se aborden los años bisiestos."""

# Definimos la función
def diasmeses(mes):
  meses = {
      'Enero' : '31',
      'Febrero': '28 0 29',
      'Marzo' : '31',
      'Abril' : '30',
      'Mayo' : '31',
      'Junio' : '30',
      'Julio' : '31',
      'Agosto' : '31',
      'Septiembre' : '30',
      'Octubre': '31',
      'Noviembre': '30',
      'Diciembre' : '31'
      }
  # Pasamos el mes del usuario a minúsculas y lo hacemos una variable
  mes = mes.capitalize()
  if mes in meses:
    diasmes = meses[mes]
  # Retornamos el valor del 
    return f'El mes {mes} tiene {diasmes} dias'
  else:
    return 'La palabra introducida no es un mes'


mes = input('Introduce un mes para ver sus dias: ')
print(diasmeses(mes))