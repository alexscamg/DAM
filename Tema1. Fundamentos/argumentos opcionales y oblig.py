import math

def opcionales(oblig_1, oblig_2, opc_1='uno', opc_2='dos', *args, **kwargs):
# *args representa una lista
# **kwargs representa a un diccionario





def superficie(radio=1):
  return radio * radio * math.pi

# s= superficie()
# print(s)

def vol_cilindro(radio, altura):
  return superficie(radio) * altura


altura = 12
v = vol_cilindro(altura)
print(v)