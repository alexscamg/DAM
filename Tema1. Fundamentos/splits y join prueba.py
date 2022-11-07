#declaramos la variable.
cadena = 'esta es una tarde*# estupenda para aprender python'
print(cadena)

#split   troceamos la variable
palabras = cadena.split()  #Entre los parentesis declaramos los separadores por lo que queramos trocear.
print(palabras)

#join  (Unimos la variable)
unidas = ''.join(palabras)  #entre la comillas ponemos el separador que queramos poner para unir.
print(unidas)


#find
posicion = cadena.find('#') #con find podemos buscar algo concreto en una cadena
print(posicion)
print(cadena[:posicion - 1])
print(cadena[posicion + 1 : ])