# 1. Escribe un programa que solicite al usuario ingresar
# un número entero y luego imprima si es positivo, negativo o cero.

numero = int(input("Ingrese un numero entero: "))

if numero == 0:
    print(f"El numero {numero} es cero")
else:
    if numero > 0:
        print(f"El numero {numero} es positivo")
    else:
        print(f"El  numero {numero} es negativo")
