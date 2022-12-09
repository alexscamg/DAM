import PySimpleGUI as ps
# Calculadora molona
menu_temas = ['menu',['SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']]
numeros = ['1','2','3','4','5','6','7','8','9','0','.']
operaciones = ['/','*','+','-']
listanumeros= []
listaoperaciones = []




def crear_ventana(tema):
  # Crear tema
  ps.theme(tema)
  boton_size = (6,3)
  ps.set_options(font='Calibri 14')


  
  #Plantilla, diseño
  layout = [
    [ps.Text('0.0',
    font='Courier 25', 
    justification='right', 
    expand_x=True,
    right_click_menu=menu_temas,
    pad=(10,30),
    key='-TEXTO-')],
    [ps.Button('Clear', expand_x=True, size=boton_size), 
    ps.Button('Enter',expand_x=True, size=boton_size, disabled=True)],
    [
      ps.Button('7', size=boton_size),
      ps.Button('8', size=boton_size),
      ps.Button('9', size=boton_size),
      ps.Button('*', size=boton_size)
    ],
    [
      ps.Button('4', size=boton_size),
      ps.Button('5', size=boton_size),
      ps.Button('6', size=boton_size),
      ps.Button('/', size=boton_size)
    ],
    [
      ps.Button('1', size=boton_size),
      ps.Button('2', size=boton_size),
      ps.Button('3', size=boton_size),
      ps.Button('-', size=boton_size)
    ],
    [
      ps.Button('0', size=boton_size,expand_x=True ,expand_y=True),
      ps.Button('.', size=boton_size),
      ps.Button('+', size=boton_size)
    ]
  ]

  return ps.Window('Calculadora', layout)

tema_defecto= 'Topanga'
window = crear_ventana(tema_defecto)

while True:
  event, values = window.read()
  if event == ps.WIN_CLOSED:
    break
  if event in menu_temas[1]:
    window.close()
    window = crear_ventana(event)
  if event in numeros:
    window['Enter'].update(disabled=False)
    listanumeros.append(event)
    num_string = ''.join(listanumeros)
    window['-TEXTO-'].update(num_string)
  
  if event in operaciones:
    listaoperaciones.append(''.join(listanumeros))
    listaoperaciones.append(event)
    listanumeros = []
    window['-TEXTO-'].update('')

  if event == 'Enter':
    listaoperaciones.append(''.join(listanumeros))
    calculo = eval(''.join(listaoperaciones))
    window['-TEXTO-'].update(f'{calculo}')
    listaoperaciones = []
    listanumeros = [str(calculo)]
    window['Enter'].update(disabled=True)
  if event == 'Clear':
    window['Enter'].update(disabled=True)
    window['-TEXTO-'].update('0.0')
    listanumeros = []
    listaoperaciones = []

#Cerrar programa
window.close()