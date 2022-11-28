import pprint
tablero = {}
color = ['Negro','Blanco']
es_negro = False

for fila in range(1,9):
    for col in ('a','b','c','d','e','f','g','h'):
        tablero[(str(fila),col)] = color[es_negro]
        if col != 'h':
            es_negro = not es_negro
    

pprint.pprint(tablero)

entrada =input('Dime la fila  y columna: ')
fila_col=tuple(entrada)
print (f'El color de la casilla ({entrada}) es {tablero[fila_col]}')