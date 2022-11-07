import pprint

# Bucles Hay dos tipos de bucles:
# for controlado por un controlador
# for variable (inicio, fin, salto)
for i in range(50, 20, -2):
    print(f'La i vale {i}')

lista = []

for i in range(20):
    lista.append(f'Elemento {i}')

pprint.pprint(lista)

largo = len(lista)

for i in range(largo):
  print(lista[i])

for x in lista:  # Esto se puede hacer cun cualquier iterable, listas, tuplas, diccionario y otras cosas.
  print(x)
# while controlado por una condicion. Siguen dando vueltas mientras se cumpla la condicion

