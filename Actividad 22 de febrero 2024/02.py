# 2. Crea un programa que pida al usuario
# dos números y luego determine si el primero es divisible por el segundo.

numero = float(input("Ingrese el primer numero: "))
numero1 = float(input("Ingrese el segundo numero: "))

if numero % numero1 == 0:
    print(f"{numero} es divisible por {numero1}")
else:
    print(f"{numero}  No es divisible por {numero1}")
