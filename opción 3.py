print("opcion 3")

print('algoritmo el cual solicite un numero entero hasta que el usuario ingrese cero. Guardar los números iterados en una lista y calcular la sumatoria y el promedio de los valores que contiene dicha lista. ')

numeros = []
suma_total = 0

while True:
    numero = int(
        input("Ingrese un número entero (ingrese 0 para terminar): "))

    if numero == 0:
        break

    numeros.append(numero)
    suma_total += numero

countador = len(numeros)
promedio = suma_total / countador if countador > 0 else 0

print("\nValores ingresados:")
for numero in numeros:
    print(numero)

print("\nSumatoria total:", suma_total)
print("Promedio total:", promedio)
