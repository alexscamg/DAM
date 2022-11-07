
contador = 10
numero =  1
for i in range(contador):
  multiplicacion = numero * numero 
  print(multiplicacion)
  numero += 1

print()

numero = 1
for i in range(10):
  resultados = numero**2 +1
  numero += 1
  print(resultados)

print()
numero = 1
for i in range(7):
  resultados = numero**3
  numero += 1
  if resultados > 1:
    print(resultados)



print()
numero = 1
for i in range(5):
  print(numero)
  multiplicacion = numero * 10
  numero= multiplicacion
  
print()
numeros = 2
res = 2
suma = 0
for c in range(7):
  print(res)
  ope1 = suma + 2
  ope2 = ope1 + numeros
  suma = ope1
  res += ope2


print()

numero = 10
for i in range(5):
  division = numero / 10
  numero = division

  print(division)

print()

numero = 0
for i in range(4):
  suma = numero + 1
  print(suma)
  resta = numero - 1
  print(resta)
