# 3. Desarrolla un programa que solicite al usuario
# ingresar un número y determine si es par o impar.

numero = int(input("Ingrese un numero:"))

if numero == 0:
    print("El numero no es cero")
elif numero % 2 == 0:
    print("El numero es par")
else:
    print("numero es inpar")
