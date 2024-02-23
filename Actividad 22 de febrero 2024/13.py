# 13. Escribe un programa que pida al usuario el radio de un circulo
# y luego calcule su área,
# pero solo si el radio es positivo.

import math

radio = float(input("Ingrese el radio del circulo: "))


if radio >= 0:
    area = math.pi * radio**2
    print(f"El area del circulo es {round(area,2)}")
else:
    print("El radio debe ser positivo")
