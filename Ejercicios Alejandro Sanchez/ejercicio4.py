"""Escriba un programa que lea una posición del usuario. 
Use una declaración if para determinar si la columna comienza con un cuadrado negro o un cuadrado blanco. 
Luego usa la aritmética modular para informar el color del cuadrado en esa fila. 
Por ejemplo, si el usuario ingresa a1, su programa debería informar que el cuadrado es negro. 
Si el usuario ingresa d5, su programa debe informar que el cuadrado es blanco. 
Su programa puede suponer que siempre se ingresará una posición válida. 
No es necesario realizar ninguna comprobación de errores."""


# Nombramos a la función.
def tableroajedrez():
  # Establezco unas lista para las casillas negras, y en cada una pongo las letras en las que la casilla es negra según si toca numero par o impar.
  impares = ['A', 'C', 'E', 'G']
  pares = ['B', 'D', 'F', 'H']
  # Le pedimos al usuario que introduzca la fila y la letras
  fila = int(input('Introduce el numero de fila: '))
  columna = input('Introduce la columna: ')
  columna = columna.upper()
  # Verificamos que la fila sea valida
  while fila <1 or fila >8:
    fila = int(input('Introduce el numero de fila: '))
  # Comprobamos si es par la fila
  if fila%2 == 0:
    # Si es par que verifique si la columna esta en la lista de impares o pares, para que nos retorne el color
    if columna in impares:
      return 'Tu casilla es: Blanca'
    else:
      return 'Tu casilla es: Negro'
  else:
    if columna in pares:
      return 'Tu casilla es: Blanco'
    else:
      return 'Tu casilla es: Negro'
  # Llamamos a la función
  
print(tableroajedrez())
  
  
  