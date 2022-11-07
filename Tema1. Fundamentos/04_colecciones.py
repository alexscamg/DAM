# Las condiciones son elemenetos que no contienen un valor, sino que contiene un cojunto de valores
# string / cadenas 
cadena = 'hola caracola'
cadena.capitalize



# list / listas 
lista = [] # siempre llevan corchetes
Lista = list()  # Otra forma de hacerlo
#list.pop()
list.append
#sum(list) #Sumamos el contenido de la lista




#dict / diccionarios
import pprint # Importamos una libreria

diccionario ={
     'uno': 'Primero', # Clave= 'uno' Valor= 'Primero'
     'dos': 'Segundo'

}
print(diccionario['uno']) # Aqui buscamos la clave y nos devuleve el valor

diccionario['tres'] = 'Tercero' # Asi añadimos contenido al diccionario

print(diccionario['tres'])
print(list(diccionario.keys())) # aqui nos muestras las claves
print(list(diccionario.values())) # Aqui nos muestra los valores del diccionario

del(diccionario['tres']) # Aqui borramos el valor que introduzcamos del diccionario

print(list(diccionario))
# ---------------------------------------------------------------------------------------------------------------------------------------
coches = {
    '5454CDP': 'Tesla Model S',
    '8345GJJ': 'Tesla Model 3',
    '5456DSF': 'Tesla Model X',
    '5465JHJ': 'Tesla MOdel y'
}

coches['7676KHG'] = 'Porsche Panamera'
print(list(coches.keys()))
pprint.pprint(coches)
persona1 = {
        'nombre' : 'Paco_1',
        'dni': '1234567L'
}
persona2 = {
        'nombre' : 'Paco_2',
        'dni': '1234567L'
}
personas = {
        1: persona1,
        2: persona2
}
pprint.pprint(personas)
#tuplas / 
mi_tupla = (1,2,3,1,2,1) # las tuplas son inmutables, no se puede modificar ningun dato de ninguna manera. solo leerlas y recorrerlas y hacer calculos. Se pueden convertir a listas y viceversa

elem = mi_tupla.count(1) # Cuantas veces aparece un valor dentro de la tupla

print('Elem: ',elem)

largo = len(mi_tupla) # vemos lo largo que es mi tupla

print('Largo: ',largo)

elem3 = mi_tupla[3] # me devuelve el valor que se encuentra en esa posicion

print('Elem3: ',elem3)

list() # Con esto podemos hacer listas y convertir tuplas en listas

#sets /
