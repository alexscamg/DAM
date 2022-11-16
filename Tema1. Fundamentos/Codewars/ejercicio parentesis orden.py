# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

"""
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""

def valid_braces(string):
  if len(string) % 2 == 1:
    return False
  parejas = {
    ')' : '(',
    ']' : '[',
    '}' : '{'
  }
  valores = list(parejas.values())
  pila = []
  for i in string:
    if i in valores:
      pila.append(i)
    else:
      ultimo = pila.pop()
      if ultimo != parejas[i]:
        return False
  if len(pila) == 0:
    return True
  else: 
    return False


