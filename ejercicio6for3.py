numero = int(input(print('Introduce un numero de filas: ')))
espacios = numero -1
caracteres = 1
for i in range(numero):
    print('\t' * espacios + '*\t' * caracteres + '\t' * espacios)
    espacios -= 1
    caracteres += 2


numero = int(input(print('Introduce un numero de filas: ')))
espacios = 0
caracteres = numero * 2 - 1
for i in range(numero):
    print('\t' * espacios + '*\t' * caracteres + '\t' * espacios)
    espacios += 1
    caracteres -= 2

