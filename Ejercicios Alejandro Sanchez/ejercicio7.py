"""Un zoológico en particular determina el precio de la entrada según la edad del visitante. 
Los huéspedes de 2 años de edad y menos se admiten sin cargo. 
Niños entre 3 y 12 años cuestan $14.00. 
Las personas mayores de 65 años o más cuestan $ 18.00. 
La entrada para todos los demás invitados es de $23.00.
Cree un programa que comience leyendo las edades de todos los invitados en un grupo del usuario, con una edad ingresada en cada línea. 
El usuario ingresará una línea en blanco para indicar que no hay más invitados en el grupo. 
Luego, su programa debe mostrar el costo de admisión para el grupo con un mensaje apropiado. 
El costo debe mostrarse con dos decimales."""


# Declaramos la función
def entradas():
  # Pedimos la edad del primer usuario
  edades = int(input('Introduce la edad de un usuario: '))
  # Declaramos los precios
  bebes = 0
  niños = 14.00
  jubilados = 18.00
  usuarios_gene = 23.00
  # Declaramos una variable para la suma de los tickets
  total = 0
  # Comprobamos que la edad no es menor que 0, ni es 0. Si es 0 o menor, volvemos a pedir la edad
  while edades <= 0:
    edades = int(input('Introduce una edad mayor que 0: '))
  # Cuando tenemos la primera edad la vamos clasificando para ver el precio de su entrada.
  while edades > 0:
    if edades <= 2:
      total += bebes
    elif edades >= 3 and edades <=12:
      total += niños
    elif edades >= 65:
      total += jubilados
    else:
      total += usuarios_gene
    # Volvemos a pedir si quiere introducir mas usuarios, si no introduce 0.
    edades = int(input('Introduce mas usuarios de tu grupo, introduce 0 si no hay mas usuarios: '))
  # Retornamos el total de las entradas
  return f'Total a pagar: {total}€'




print(entradas())