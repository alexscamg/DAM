# Pedimos dos numeros al usuario

dividendo = int(input('Introduce un dividendo: '))
divisor = int(input('Introduce un divisor: '))

# Ahora vemos si el divisor es cero, para indicar que no se puede dividir por cero
# Si no es cero seguira y hara la operacion
if divisor != 0:
    cociente = dividendo // divisor
    resto = dividendo % divisor

    if resto == 0:
      print(cociente)

    else:
      print('El cociente es: ',cociente)
      print('el resto es: ',resto)

else:
  print('No se puede dividir por cero')