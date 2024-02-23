# 12. Elabora un programa que determine si un año ingresado por el usuario
# es un año de jubilación (mayor o igual a 65 años).

nacimiento = int(input("Ingresa el año en naciste:"))
anio_actual = int(input("Ingresa el año que actual: "))

if anio_actual - nacimiento >= 65:
    print("Felicidades te puedes jubilar")
else:
    print("Aun te falta para jubilarte")
