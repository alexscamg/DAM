# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
import string

def alphabet_position(text):
  text = text.lower()
  abc = string.ascii_lowercase
  salida = []
  for i in text:
    idx = abc.find(i)
    if idx > -1:
      salida.append(str(idx + 1))

  return ' '.join(salida)


print(alphabet_position('abcdefgh'))