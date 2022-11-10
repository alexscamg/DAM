def pinta_tabla():
  filas = 10
  cols = 10
  tabla = [
    [1,2,3,4,5,6,7,8,9,0],
    [0,9,8,7,6,5,4,3,2,1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [0, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  ]
  for f in tabla:
    for c in f:
      print(f'{c}\t',end='')
    print()



pinta_tabla()