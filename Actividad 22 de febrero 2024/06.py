# 6. Crea un programa que solicite al usuario ingresar la longitud de los lados de un triángulo y
# determine si es equilátero, isosceles o escaleno

lado1 = int(input("Ingrese el primer lado del triangulo:"))
lado2 = int(input("Ingrese el segundo lado del triangulo:"))
lado3 = int(input("Ingrese el tercer lado del triangulo:"))

if lado1 == lado2 and lado1 == lado3:
    print("el triangulo es equilatero")
elif lado1 != lado2 and lado2 != lado3:
    print("El triangulo es escaleno")
else:
    print("El triangulo es isosceles")
