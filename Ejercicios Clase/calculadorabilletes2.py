import pprint

billetes = [500, 200, 100, 50, 20, 10, 5, 2, 1]


def calculadora_billetes(numero):
    desglose = {}

    for i in billetes:
        desglose[i] = numero // i
        numero = numero % i

    pprint.pprint(desglose)

    for k, v in desglose.items():  # .item nos permite trabajar con el interior del diccionario por los valores separados
        if v > 0:                     # Ponemos dos variables una para las claves y otra para los valores en este caso
            print(f'{v} X {k}')


calculadora_billetes(17_342)
calculadora_billetes(500)



