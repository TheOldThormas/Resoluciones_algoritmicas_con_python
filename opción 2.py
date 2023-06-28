print("opcion 2")
print('algoritmo en el cual se solicite ingresar un numero entero y de acuerdo al número ingresado imprimir si es positivo, negativo o igual a cero ejecutar algoritmo hasta que el usuario ingrese "*"')


def check_number(numero):
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es igual a cero.")


while True:
    numero = input("Ingrese un número entero (o ingrese '*' para salir): ")

    if numero == "*":
        print(" ya salio del programa :)  ")
        break

    try:
        numero = int(numero)
        check_number(numero)
    except ValueError:
        print("Porfa profe ingrese un número entero válido!!.")
