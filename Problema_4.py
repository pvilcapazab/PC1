#Poner en contexto al usuario
print("-Suma de los primeros N número naturales-")

#Guardar en una variable el valor de N
n = int(input('Introduzca N: '))

#Verificar si 'n' es un número positivo
if n > 0:
    #Calcular la suma de los N primeros números naturales (1 + 2 + 3 + ... + N)
    suma = n * (n+1) / 2

    #Imprimir la suma resultante
    print("La suma es:", suma)
else:
    print("Por favor, introducir solo números enteros y positivos")