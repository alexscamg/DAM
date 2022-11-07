# Las funciones informáticas son una manera de reutilizar el código. 

# Sintaxis
def nombrefuncion(): # Los paréntesis son obligatorios. dentro de ellos se pueden pone los parámetros para que son un valor que le paso a la función para    que  haga sus calculos
  print('hola')        # Cada función debe de hacer una sola cosa y hacerla bien.
# Una función no debe de saber nada del mundo exterior.(IMPORTANTE) Una función tiene alta cohesion y bajo acoplamiento.
nombrefuncion()
# Una variable que está dentro de una función, no se conoce fuera de la función.
def saludo(nombre, dia):
  print(f'Buenas tardes, {nombre}. Hoy es {dia}.')

saludo('Alejandro','Lunes') # El argumento es el valor que le damos al parámetro cuando llamamos a la función, en este caso Alejandro


def inversa(cadena):
  print(cadena[::-1])




def inversa(cadena):
  return cadena[::-1] # [::-1] le da la vuelta al texto y lo devuelve a quien lo haya invocado

x= inversa ('hola')

print(x)





palabras = ['uno','dos','tres']

for p in palabras:
  x = inversa(p)
  print(x)



def cuenta_vocales(cadena):
  vocales = {}
  letras = 'aeiou'

  for c in letras:
    vocales[c] = cadena.lower().count(c)

  return vocales

texto = 'Hola que tal estas'
x = cuenta_vocales(texto)

print(x)



def saluda():
  nombre = gente[1]
  print(f'Hola, {nombre}')

gente = ['Ana', 'Miguel', 'Dani']
saluda()

# Una función no debe de saber nada del mundo exterior.(IMPORTANTE) Una función tiene alta cohesion y bajo acoplamiento.


def saluda2(personas):
    for p in personas:
      print(f'Hola, {p}')

gente2 = ['Ana', 'Miguel', 'Dani']
saluda2(gente2)




def saluditos(kiwi):
  salida = []
  for p in kiwi:
    salida.append(f'Hola, {p}')

  return salida


gente = ['Ana', 'Miguel','Dani']

saludos = saluditos(gente)
print(saludos)




def suma(a, b):
  return a + b


resultado = suma(1,2)
print(resultado)


