# 9. Escribe un programa que determine si un número
# ingresado por el usuario es primo o no.

numero = int(input("Ingresa un numero: "))

if numero % numero == 0 and numero % 1 == 0 and numero != numero % numero != 0:
    print(f"el numero es primo")
else:
    print("No es primo")
