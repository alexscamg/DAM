"""Escriba un programa que solicite al usuario que ingrese 5 números, separados por comas. 
Calcule la suma de los 5 números y muestre los números ingresados y la suma al usuario.
"""
# Definimos la función
def suma():
  # Pedimos los numeros al usuario y declaramos las variable suma y el separador
  numero = input('Introduce 5 numeros separados por coma: ')
  suma = 0
  separador = ','
  largo = len(numero)
  # Recorremos la cadena y la troceamos por el separador indicado
  for i in numero:
    numeros = numero.split(separador)
  # Recorremos la lista y vamos sumando los valores
  for n in range(5):
    num = numeros[n]
    suma += int(num)
  return suma
      


print(suma())
