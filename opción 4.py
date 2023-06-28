print("opción 4")

print('algoritmo que pida un numero entero al usuario y muestre la suma de todos los dijitos de dicho número ')


def sum_digits(numero):
    suma_total = 0
    for digitos in str(numero):
        suma_total += int(digitos)
    return suma_total


numero_de_usuario = input("Ingrese un número entero: ")
try:
    numero = int(numero_de_usuario)
    suma_digitos = sum_digits(numero)
    print("La suma de los dígitos es:", suma_digitos)
except ValueError:
    print("Error: Ingrese un número entero válido.")
23112
