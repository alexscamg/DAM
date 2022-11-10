"""Comúnmente se dice que un año humano equivale a 7 años caninos. 
Sin embargo, esta simple conversión no reconoce que los perros alcanzan la edad adulta en aproximadamente dos años. 
Como resultado, algunas personas creen que es mejor contar cada uno de los dos primeros años humanos como 10,5 años caninos y luego contar cada año humano adicional como 4 años caninos.
Escriba un programa que implemente la conversión de años humanos a años caninos descrita en el párrafo anterior. 
Asegúrese de que su programa funcione correctamente para conversiones de menos de dos años humanos y para conversiones de dos o más años humanos. 
Su programa debería mostrar un mensaje de error apropiado si el usuario ingresa un número negativo."""


# Definimos la función
def añosperro(añoshum):
    # Creamos una variable que nos guarde los años del perro
    añosper = 0
    # Indicamos que mientras el usuario introduzca 0 o menos siga pidiendole una edad
    while añoshum <= 0:
        añoshum = float(input('Introduce un numero positivo: '))
        # Aqui comprobamos si los años son iguales a dos o menos para calcular la edad directamente
    if añoshum <= 2:
        añosper = añoshum * 10.5
        return añosper
        # Si es mayor que dos que calcule los 2 primeros años y el resto y  haga el total
    elif añoshum > 2:
        resta = añoshum - 2
        añosres = resta * 4
        primerosaños = 2 * 10.5
        return añosres + primerosaños

# Pedimos al usuario la edad de su perro
años = float(input('Introduce los años humanos de tu perro: '))
# Nombramos a la función
print(añosperro(años))
