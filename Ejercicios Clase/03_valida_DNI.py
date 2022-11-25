"""
letras validas: TRWAGMYFPDXBNJZSQVHLCKE
dni valido:
    - Longitud de 8:
    - La letra sera valida si el indice coincide con el resto de la division entera de numero entre 23
"""


def calcula_letra(dni):
  letras_validas = 'TRWAGMYFPDXBNJZSQVHLCKE'
  return letras_validas[dni%23]

def valida_dni(dni):
  return len(dni) == 9 and calcula_letra(int(dni[:8])) == dni[8].upper()


dni = '28847881Q'
# print(calcula_letra(dni))



print(valida_dni(dni))
