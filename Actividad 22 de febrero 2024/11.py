# 11. Desarrolla un programa que solicite al usuario ingresar
# tres notas y luego calcule el promedio,
# indicando si es aprobado (promedio >= 3) o reprobado (promedio < 3).

nota1 = float(input("Ingresa la primera nota:"))
nota2 = float(input("Ingresa la primera nota:"))
nota3 = float(input("Ingresa la primera nota:"))

promedio = (nota1 + nota2 + nota3)/3

if promedio >= 3:
    print(f"El alumno Aprobo {promedio}")
else:
    print(f"El alumno repobo {round(promedio,3)}")
