import os 

RUTA_BASE = os.getcwd()
ARCHIVO = 'todo.csv'
RUTA_COMPLETA = os.path.join(RUTA_BASE , ARCHIVO)

print(RUTA_BASE)
print(RUTA_COMPLETA)