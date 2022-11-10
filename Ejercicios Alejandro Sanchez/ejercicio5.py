"""En este ejercicio, creará un programa que calcule el promedio de una colección de valores ingresados por el usuario. 
El usuario ingresará 0 como valor centinela para indicar que no se proporcionarán más valores. 
Su programa debería mostrar un mensaje de error apropiado si el primer valor ingresado por el usuario es 0."""


# Declaramos la función
def promedio():
  # Pedimos un numero para calcular el promedio
  numeros = int(input('Introduce un numero para calcular el promedio: '))
  # Aquí vamos sumando los números
  suma = 0
  # Aquí vamos apuntando cuantos números hemos introducido
  factores = 0
  # Si es un numero negativo nos sigue pidiendo el numero
  while numeros <0:
    numeros = int(input('Introduce un numero mayor que cero: '))
  # Vemos si el numero es igual que 0, si es asi decimos que no se puede calcular el promedio de 0
  if numeros == 0:
    return 'No se puede calcular el promedio de 0'
  # Si el numero no es 0, procedemos a sumar el numero al total y a apuntar que se ha introducido un numero
  while numeros != 0:
    suma += numeros
    factores +=1
    # Volvemos a pedir otro numero
    numeros = int(input('Introduce otro numero: '))
  # Calculamos el promedio
  return suma/factores

  




print(promedio())