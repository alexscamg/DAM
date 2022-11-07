def alumno_notas(alumno, *asignaturas):
  print(f'El alumno {alumno} se ha matriculado de las asignaturas: ')
  print('--------------------')
  for a in asignaturas:
    print(a)

#asig = ['programación', 'BD', 'Sistemas', 'Filologia']
#alumno_notas('Miguelito de la roda')


def alumno_notas2(alumno, *asignaturas, **notas):
  print(f'El alumno {alumno} se ha matriculado de las asignaturas: ')
  print('--------------------')
  for a in asignaturas:
    print(a)
  print('----------------')
  print('Sus notas son: ')
  for k,v in notas.items():
    print(f'{k}: {v}')


alumno = 'Miguelito de la roda'
asig = ['programación', 'BD', 'Sistemas', 'Filologia']
notas = {
  'Programación' : 7, 
  'BD' : 2.5, 
  'Sistemas' : 5,
}
alumno_notas2(alumno, *asig, **notas)
