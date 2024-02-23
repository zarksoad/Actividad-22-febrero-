# 8. Elabora un programa que solicite al usuario ingresar
# tres númeras y luego imprima si estos pueden formar un triángulo välido.

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

if numero1 + numero2 > numero3 and numero1 + numero3 > numero2 and numero2 + numero3 > numero1:
    print("Los números pueden formar un triángulo válido.")
else:
    print("Los números no pueden formar un triángulo válido.")
