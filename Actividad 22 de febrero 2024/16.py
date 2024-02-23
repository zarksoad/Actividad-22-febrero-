# 16. Escribe un programa que solicite al usuario
# el nombre de un mes y luego imprima la cantidad de dias que tiene ese mes.
mes = input("Ingrese el nombre de un mes en minúsculas:")
dias_por_mes = {
    "enero": 31,
    "febrero": 28,
    "marzo": 31,
    "abril": 30,
    "mayo": 31,
    "junio": 30,
    "julio": 31,
    "agosto": 31,
    "septiembre": 30,
    "octubre": 31,
    "noviembre": 30,
    "diciembre": 31
}

if mes in dias_por_mes:
    print(f"El mes de {mes} tiene {dias_por_mes[mes]} días.")
else:
    print("MPor favor  ingrese el nombre de un mes válido en minúsculas.")