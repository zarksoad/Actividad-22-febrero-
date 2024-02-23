
#2 programa que imprime el mayor el medio y el menor

numero1 = int(input("Ingrese un numero:"))
numero2 = int(input("Ingrese un numero:"))
numero3 = int(input("Ingrese un numero:"))



if numero1 == numero2 and numero1 == numero3:
    print("Los numeros son iguales")
elif numero1 > numero2 and numero1 > numero3 and numero2 > numero3 :
    print(f"el numero {numero1} es el mayor")
    print(f"el numero {numero2} es el del medio")
    print(f"el numero {numero3} es el menor")
elif numero2 > numero1 and numero2 > numero3 and numero1 > numero3 :
    print(f"el numero {numero2} es el mayor")
    print(f"el numero {numero1} es el del medio")
    print(f"el numero {numero3} es el menor")
elif numero3 > numero1 and numero3 > numero2 and numero1 > numero2 :
    print(f"el numero {numero3} es el mayor")
    print(f"el numero {numero1} es el del medio")
    print(f"el numero {numero2} es el menor")     
else:
    print("uno de los no cumple las condiciones")    