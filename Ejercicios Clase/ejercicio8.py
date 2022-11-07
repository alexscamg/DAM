import math

# pedir los coeficioentes de una ecuacion de segundo 
# grado y que muestre las soluciones

a = int(input('Introduce a: '))
b = int(input('Introduce b: '))
c = int(input('Introduce c: '))

# Operaciones
cuadradob = b*b
raiz = cuadradob -4 * a * c
a2 = 2 * a
if a == 0:
   if b == 0:
      print('Sin solucion')
   else:
    solucion1 = -c/b 

else:
  if raiz >= 0:
    solucionpos = ((-b + math.sqrt(raiz))/a2)
    solucionneg = ((-b - math.sqrt(raiz))/a2)
    if solucionpos == solucionneg
      print(f'Una solucion {solucionpos}')
    else:
      print(f'Las soluciones de la ecucacion son {solucionpos} y {solucionneg}')
  else:
    print('No tiene solucion')