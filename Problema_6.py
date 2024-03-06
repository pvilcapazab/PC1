#Solicitar la edad del cliente
edad = int(input("Introduzca su edad: "))

#Mostrar el precio de la entrada por edades
if 0 <= edad < 4:
    print("¡La entrada es gratuita!")
elif 4 <= edad <= 18:
    print("El precio de la entrada es: $5")
elif 18 < edad:
    print("El precio de la entrada es: $10")
else:
    #Si se introduce una edad menor de 0, se imprimirá el siguiente error
    print("Opción inválida")