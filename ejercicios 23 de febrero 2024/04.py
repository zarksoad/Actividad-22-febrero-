#Elabore  un algoritmo  que lea un numero <32768 y que efectue la operacion si es multiple de cuatro imprimir dividivo por 4 
# si es multiplo del 5 imprimir la quinta parte del numero elevado al cuadrado, si es multiplo de 7 imprimeir el numero dividido por 8 
# si no es multiple imprimir numero extraño 
numero = int(input("Ingrese un numero:"))

if numero < 32768:
    if numero % 4 == 0 and numero %5 != 0:
        print(f" el numero es multiplo de 4 el {numero} dividio por 4 es: {numero / 4}")
    elif numero %5 == 0:
        print((numero / 5 )**2)
    elif numero %7 == 0:
        print(numero /8)   
    else:
        print("Numero extraño")
else:
    print("el numero no cumple con las condiciones")    