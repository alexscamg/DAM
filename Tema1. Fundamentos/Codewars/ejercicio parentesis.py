# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python



def duplicate_encode(word):
  lword = word.lower()
  salida = ''
  for i in lword.lower():
    ct = lword.count(i)
    if ct == 1:
      salida += '('

    else:
      salida += ')'

  return salida


    




print(duplicate_encode('CodeWarrior'))

