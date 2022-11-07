cadena = "En un lugar de la Mancha..."
print(cadena)
print(len(cadena)) #Saber sabemos que longitud tiene la cadena

print(cadena.capitalize()) #Pone la primera letra en mayuscula

print(cadena.swapcase())#Intercambia mayusculas por minusculas y viceversa

print(cadena.replace("la", "lo"))

print(cadena.title())#Como capitalice pero con cada palabra

print(cadena.split()) #Convierte una cadena en una lista

cadena = "1,2,3,4,5,6,7"

trozos = cadena.split(',')

unida = '<>'.join(trozos)

print(unida)