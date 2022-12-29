import pprint

# Diccionarios
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
    '5465JHJ': 'Tesla Model y'
}

coches['7676KHG'] = 'Porsche Panamera'
print(list(coches.keys()))
pprint.pprint(coches)


# con index se busca en los diccionarios