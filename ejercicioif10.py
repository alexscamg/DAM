centimetros = 240005
km = centimetros // 100_000
restokm = centimetros % 100_000 //100
cm = centimetros // 100


if centimetros >1000:
  print(f'{km} KM. {restokm}m.{cm}')

elif restokm >100:
  print(f'{restokm}m.')
else:
  print(f' {centimetros} cm.')


