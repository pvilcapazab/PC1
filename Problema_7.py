#Preguntar por la operación que desea realizar
operador = input("Ingrese la operación que desee realizar (+, -, *): ")

#Solicitar los números que se van a operar
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

#Según la operación deseada, se realizaran los calculos
if operador == "+":
    print(f"La suma de {a} + {b} = {a+b}")
elif operador == "-":
    print(f"La resta de {a} - {b} = {a-b}")
elif operador == "*":
    print(f"La multiplicación de {a} * {b} = {a*b}")
else:
    #Si se introduce un operador que no está en la lista, se mostrará el siguiente error
    print(f"El operador es inválido")