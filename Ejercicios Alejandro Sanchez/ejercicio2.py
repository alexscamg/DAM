"""Escriba un programa que determine el nombre de una forma a partir de su número de lados.
Lea la cantidad de lados del usuario y luego informe el nombre apropiado como parte de un mensaje significativo. 
Su programa debe admitir formas con entre 3 y 10 lados (incluidos). 
Si se ingresa un número de lados fuera de este rango, su programa debería mostrar un mensaje de error apropiado."""

# Definimos la función que nos dará la figura
def poligonos(lados):
  # Creamos un diccionario con las figuras
  formas = { 
    3: "Triangulo",
    4: "Cuadrado",
    5: "Pentágono",
    6: "Hexaedro",
    7: "Heptágono",
    8: "Octógono",
    9: "Eneagono",
    10: "Decagono" 
    }
  # Filtramos si tiene menos de 3 lados o mas de 10
  if lados <3 or lados>10:
    return 'Tu figura no es valida'
  # Si se encuentra dentro de los valores nos dará la figura correspondiente del diccionario
  else:
    poligono = formas[lados]
    return f'Tu figura es {poligono}'




figura = int(input('Introduce el numero de lados: '))
print(poligonos(figura))