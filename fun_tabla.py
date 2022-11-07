def pinta_tabla(filas, cols):
  cadena = '<tables>'
  for f in range(filas):
    cadena += '<tr>'
    for c in range(cols):
      cadena += f'<td>({f},{c})</td>'
    cadena += '</tr>'

  cadena += '</tables>'
  return cadena

print(pinta_tabla(10,10))