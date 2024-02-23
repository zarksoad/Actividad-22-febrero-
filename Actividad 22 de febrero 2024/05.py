# 5. Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.

def anio_bisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        print(f"El año {anio} es bisiesto")
    else:
        print("No es bisiesto")


valor = int(input("Ingrese un año:"))
anio_bisiesto(valor)
