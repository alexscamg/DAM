"""Escriba un programa que solicite al usuario que ingrese 5 números, separados por comas. 
Calcule la suma de los 5 números y muestre los números ingresados y la suma al usuario.
"""

def suma():
  numero = input('Introduce 5 numeros separados por coma: ')
  suma = 0
  separador = ','
  largo = len(numero)
  while largo != 14:
    numero = input('¡Error! Introduce 5 numeros separados por coma: ')
    largo = len(numero)
  for i in numero:
    numeros = numero.split(separador)
    
  for n in range(5):
    num = numeros[n]
    suma += int(num)
  return suma
      


print(suma())
