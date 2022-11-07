nota = int(input(('Introduce un numero: ')))

# Sentencias
if nota < 5:
    print('Ha suspendido')
elif nota < 7:
    print('Ha aprobado')
elif nota < 9:
    print('Ha sacado un notable')
else:
    print('Ha sacado un sobresaliente')
