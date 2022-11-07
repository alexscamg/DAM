def suma_muchos(*args):  # Nos indica una lista de argumentos y podemos ponerle tantos argumentos como queramos. También indica que son opcionales
  total = 0
  for i in args:
    total += i
  return total 


# print(suma_muchos(1,2,3,4,5,6,7,8,12,21,21))

def encadenar(separador, *args):
  """
  Concatena las cadenas contenidas en args y las separa con el separador
  """
  lista = list(args)
  return separador.join(args)


separador = '*'
# print(encadenar(separador, '1','2','3','4','5','6','7','8','9'))




# ----------------
# 1. Pedimos lista de cadenas
# 2. Pedimos separador
# 3. Llamamos el resultado
# 4. Imprimimos el resultado


palabras = []
while True:
  entrada = input('Dime una palabra: ')
  if entrada == '':
    break
  else: 
    palabras.append(entrada)

sep = input('Dime un separador: ')
print(encadenar(sep,*palabras))