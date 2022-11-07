"""Escriba un programa que lea una posición del usuario. 
Use una declaración if para determinar si la columna comienza con un cuadrado negro o un cuadrado blanco. 
Luego usa la aritmética modular para informar el color del cuadrado en esa fila. 
Por ejemplo, si el usuario ingresa a1, su programa debería informar que el cuadrado es negro. 
Si el usuario ingresa d5, su programa debe informar que el cuadrado es blanco. 
Su programa puede suponer que siempre se ingresará una posición válida. 
No es necesario realizar ninguna comprobación de errores."""



def tableroajedrez():

  impares = ['A', 'C', 'E', 'G']
  pares = ['B', 'D', 'F', 'H']
  fila = int(input('Introduce el numero de fila: '))
  columna = input('Introduce la columna: ')
  columna = columna.upper()
  if fila%2 == 0:
    if columna in impares:
      return 'Tu casilla es: Blanca'
    else:
      return 'Tu casilla es: Negro'
  else:
    if columna in pares:
      return 'Tu casilla es: Blanco'
    else:
      return 'Tu casilla es: Negro'
  
print(tableroajedrez())
  
  
  