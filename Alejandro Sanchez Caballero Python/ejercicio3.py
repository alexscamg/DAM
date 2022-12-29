"""
Ingresa una lista de números enteros y calcula la suma de los números pares  y la suma de los impares. Introduce una cadena vacia (intro) para que deje de pedirte numeros y haga el calculo      Alejandro Sanchez Caballero
"""

def ingresa_numero():
  lista_numeros = []
  while True:
    numero = input('Introduce un numero entero: ')
    if numero == '':
        break
    else:
      try:
          numero = int(numero)
          lista_numeros.append(numero)
      except:
          print('Introduce un numero entero, por favor') 
          continue
  return lista_numeros


def calcula(numeros):
  suma_pares = 0
  suma_impares = 0
  for numero in numeros:
    if numero % 2 == 0:
      suma_pares += numero
    else:
      suma_impares += numero

  return f'La suma de los numeros pares es: {suma_pares} \nLa suma de los numeros impares es: {suma_impares}'





print(calcula(ingresa_numero()))