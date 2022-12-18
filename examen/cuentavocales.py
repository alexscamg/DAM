

texto = input('Introduce un texto: ')

def cuenta_vocales(texto):
  vocales_texto = []
  vocales = ['a','e','i','o','u']
  for i in texto:
    i = i.lower()
    if i in vocales and i not in vocales_texto:
      vocales_texto.append(i)
    
    
  return vocales_texto



print(cuenta_vocales(texto))