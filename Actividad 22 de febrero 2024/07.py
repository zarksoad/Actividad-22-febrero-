# 7. Desarrolla un programa que pida al usuario ingresar tres edades y
# luego determine cuál es la menor de ellas.


edad1 = int(input("Ingresa la primera edad:"))
edad2 = int(input("Ingresa la segunda edad:"))
edad3 = int(input("Ingresa la tercera edad:"))

if edad1 < edad2 and edad1 < edad3:
    print(f"La primera edad es menor: {edad1}")
elif edad2 < edad1 and edad2 < edad3:
    print(f"La segunda edad es menor: {edad2}")
elif edad3 < edad1 and edad3 < edad2:
    print(f"La tercera edad es menor: {edad3}")
else:
    print("No hay edad menor")
