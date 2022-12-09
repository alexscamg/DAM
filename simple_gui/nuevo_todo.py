import PySimpleGUI as ps
import csv
from config import RUTA_COMPLETA


ps.theme('LightGray1')
ps.set_options(font='Calibri 12', button_element_size=(3,2))

def lee_fichero(nombre_archivo):
    with open (nombre_archivo) as f:
        lector = csv.reader(f)
        cabecera = next(lector)
        datos = list(lector)
    return cabecera, datos

def escribe_fichero(nombre_archivo, cabecera, datos):
    with open(nombre_archivo, 'w') as f:
        escritor = csv.writer(f)
        escritor.writerow(cabecera)
        escritor.writerow(datos)




def main_windows ():
    cab, datos = lee_fichero(RUTA_COMPLETA)
    layout = [                                #CREACION DEL LAYOUT
        [ps.InputText('',key='-ID-'),
        ps.InputText('', key='-EDITOR-'),
        ps.Checkbox('Hecho', key='-HECHO-', default=False),
        ps.Text(),ps.Button('OK'),
        ps.Button('Cancelar')],
        [ps.Table(
            headings=cab,
            values=datos,
            auto_size_columns=True,
            expand_x=True,
            expand_y=True,
            enable_events=True,
            enable_click_events=True,
            key='-TABLA-'
        )]
    ]
    
    window = ps.Window('TODO', layout, resizable=True) #CREACION DE VENTANA 
    while True:
        event, values = window.read()
        if event == ps.WIN_CLOSED:
            break
            
        if event[0] == '-TABLA-':
            fila = datos[event[2][0]]
            window['-ID-'].update(fila[0])
            window['-EDITOR-'].update(fila[1])
            if fila[2].strip() == 'Hecho':
                window['-HECHO-'].update(True)
            else:
                window['-HECHO-'].update(False)

main_windows()

""" cab, datos = lee_fichero(RUTA_COMPLETA)
print(cab)
print(datos)
escribe_fichero(RUTA_COMPLETA, cab, datos) """