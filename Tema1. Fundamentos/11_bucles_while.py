control = 0
mensaje = 'este es un experimento de while'

"""
# break 
while control < 15:
  if mensaje[control] == 'x':
    break                      # su resultado dependerá de en que parte del código se encuentre y ROMPE el bucle
  print(mensaje[control])
  control += 1

print('He salido del bucle')
"""



# continue


while control < len(mensaje):
  control += 1
  if mensaje[control] == 'e':
    continue                      # su resultado dependerá de en que parte del código se encuentre y CONTINUE se salta todo el código hasta el final y volver a empezar
  print(mensaje[control])
  

print('He salido del bucle')
# exit - Para salir de un programa directamente


