base = 5
altura = 4
espacio = '\t' *(base -2)

"""
print('*\t'+'*\t''*\t'+'*\t''*\t')
print('*\t'+'\t''\t'+'\t''*\t')
print('*\t'+'\t''\t'+'\t''*\t')
print('*\t'+'*\t''*\t'+'*\t''*\t')
"""
linea_base = '*\t' * base
linea_media = '*\t'+ espacio + '*'


print(linea_base)

for i in range(altura-2):
  print(linea_media)

print(linea_base)