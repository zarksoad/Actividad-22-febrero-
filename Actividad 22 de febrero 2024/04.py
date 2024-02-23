# 4. Elabora un programa que
# pida al usuario tres números y Luego imprima el mayor de ellos.


numero = int(input("Ingresa el primer numero:"))
numero1 = int(input("Ingresa el segundo numero:"))
numero2 = int(input("Ingresa el tercer numero:"))

if numero > numero1 and numero > numero2:
    print(f"El numero {numero} es mayor")
elif numero1 > numero and numero1 > numero2:
    print(f"El numero {numero1} es mayor")
elif numero2 > numero and numero2 > numero1:
    print(f"El  numero es mayor {numero2}")
else:
    print("No hay numero mayor")
