import os
import PySimpleGUI as ps


RUTA_BASE =os.getcwd()
archivo = 'todo.csv'
ESTADOS = ['Pendiente', 'Hecho']


def leer_archivo():
    salida = []
    with open(os.path.join(RUTA_BASE, archivo),'r') as f:
        for linea in f:
            tarea = {}
            elementos = linea.split(',')
            tarea['id'] = elementos[0].strip()
            tarea['desc'] = elementos[1].strip()
            tarea['estado'] = elementos[2].strip()
            salida.append(tarea)

    return salida


def escribir_tareas(datos):
    txt = ''
    for d in datos:
        l = list(d.values())
        txt += f'{l[0]}, {l[1]}, {l[2]}\n'
    
    with open(os.path.join(RUTA_BASE, archivo),'w') as f:
        f.write(txt)


def mayor_id(tareas):
    max_id = 0
    for elem in tareas:
        if int(elem['id']) > max_id:
            max_id = int(elem['id'])
    return max_id

  
def listar_tareas(tareas,estado=None):
    print('TODAS LAS TAREAS')
    print('----------------\n')
    for t in tareas:
        if estado != None:
            if t["estado"] == estado:
                print(f'{t["id"]}: {t["desc"]} - {t["estado"]}')
        else:
            print(f'{t["id"]}: {t["desc"]} - {t["estado"]}')
    print()
    print()


def nueva_tarea(tareas):
    limpia_pantalla()
    print('NUEVA TAREA')
    print('-----------')
    desc = input('Descripción: ')
    id = mayor_id(tareas) + 1
    estado = ESTADOS[0]
    nt ={'id':id, 'desc':desc,'estado': estado} 
    tareas.append(nt)
    

def editar_tarea(tareas, id):
    for t in tareas:
        if t['id'] == str(id):
            nueva_desc = input(f"Desc: [{t['desc']}]: ")
            nuevo_estado = input(f"Estado: [{t['estado']}]: 0->Pendiente, 1-> Hecho: ")
            if nueva_desc !='':
                t['desc'] = nueva_desc
            if nuevo_estado != '':
                t['estado'] = ESTADOS[int(nuevo_estado)]


def borrar_tarea(tareas, numero):
    for t in tareas:
        if t['id'] == numero:
            tareas.remove(t)

def pinta_menu():
    print('MENÚ PRINCIPAL')
    print('-'*20)
    print('1. Lista de tareas')
    print('2. Nueva tarea')
    print('3. Editar tarea')
    print('4. Borrar tarea')
    print('5. Mostrar tarea por estado')
    print('6. Salir')
      

def limpia_pantalla():
    os.system('clear')


def main():

    limpia_pantalla()
    pinta_menu()
    todos = leer_archivo()
    while True: 
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            limpia_pantalla()
            listar_tareas(todos)
            pinta_menu()

            

        if opcion == 2:
            nueva_tarea(todos)
            escribir_tareas(todos)
            todos = leer_archivo()
            limpia_pantalla()
            pinta_menu()

        if opcion == 3:
            numero = int(input('Introduzca el número de la tarea a editar: '))
            editar_tarea(todos,numero)

            escribir_tareas(todos)
            todos = leer_archivo()
            limpia_pantalla()
            pinta_menu()

        if opcion == 4:
            numero = input('Introduzca el número de la tarea a borrar: ')
            borrar_tarea(todos,numero)
            escribir_tareas(todos)
            todos = leer_archivo()
            limpia_pantalla()
            pinta_menu()


        if opcion == 5:
            numero = int(input('Introduzca el estado [0-> Pendiente, 1-> Hecho]: '))
            estado = ESTADOS[numero]
            limpia_pantalla()
            listar_tareas (todos,estado)
            pinta_menu()


        if opcion == 6:
            exit()

def main_window():

    layout = [
        [ps.Text('1'),
        ps.InputText(),
        ps.Button('OK'), 
        ps.Button('Cancel')],
        [ps.Multiline(size=(80,25))]
    ]

    #todos = leer_archivo()

    window = ps.Window('Todo', layout)
    while True:
        event, values = window.read()
        if event == ps.WIN_CLOSED:
            break

main_window()