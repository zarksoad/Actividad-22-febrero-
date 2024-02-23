#Elabore un programa que lea tres numero y que solo imprima el mayor:_

numero1 = int(input("Ingrese un numero:"))
numero2 = int(input("Ingrese un numero:"))
numero3 = int(input("Ingrese un numero:"))



if numero1 == numero2 and numero1 == numero3:
    print("Los numeros son iguales")
elif numero1 > numero2 and numero1 > numero3:
    print(f"el numero {numero1} es el mayor")
elif numero2 > numero1 and numero2 > numero3:
    print(f"el numero {numero2} es el mayor")
elif numero3 > numero2 and numero3 > numero1:
    print(f"el numero {numero3} es el mayor")        
else:
    print("Numero invalido")    


