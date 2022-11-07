from readline import insert_text


mi_lista = [1,2,3,4, 'hola',True,['a','b','c']] # Asi hacemos listas          Las listas siempre se van llenado desde el final

mi_lista.append('otro') # Manera de meter cosas en las listas

mi_lista.extend([7,8,9]) # Este metodo es para meter valores iterables, valores que se pueden recorrer

mi_lista.insert(4,'nuevo dato')  # Con este podemos añadir datos en cualquier parte de uno en uno al igual que en append

mi_lista = mi_lista + ['k','l','m'] + [1,4,7]  # sumamos a la lista mas cosas. Como si fuera un extend

x = mi_lista.pop() # nos saca el ultimo elemento de la lista y nos lo muestra, Lectura destructiva, no es revesible. si quieres añadirlo a la lista, haces un append de la variavle que hayamos indicado
print('X: ' ,x)

lector = mi_lista[5]      # esto es una lectura no destructiva, nos muestra el valor indicado de la lista
print('Lector: ',lector)

print(mi_lista)

list() # Con esto podemos hacer listas y convertir tuplas en listas

