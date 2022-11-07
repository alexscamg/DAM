#Tipos mutables (Listas)

#Tipos inmutables ( Numeros, Cadenas de texto)


numero = 0
#cadena = 'Hola'
#cadena = 'adios'

#Entrada
cadena = 'Esto es un experimento con cadenas'
#Encontramos la longitud de la cadena
largo = len(cadena)

print(len(cadena))
#Encontramos en que posicion se encuentra nuestra palabra
posicion = cadena.find('experimento')
print(posicion)

#Una vez tenemos la posicion, cambiamos la palabra
corte = '--------------------'
print(corte)
#salida
#cadena = 'Esto es un EXPERIMENTO con cadenas'

#----------------------------
palabra = 'experimento'
longitud = len(palabra)
pto1 = cadena.find(palabra)
pto2 = pto1 + longitud


parte1 = cadena[:pto1]
parte2 = palabra.upper()
parte3 = cadena[pto2:]

resultado = parte1 + parte2 + parte3

print(resultado)