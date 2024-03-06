#Solicitar la cantidad de payasos y muñecas vendidos
cantidad_payasos = int(input("Ingrese la cantidad de payasos vendidos: "))
cantidad_munecas = int(input("Ingrese la cantidad de muñecas vendidas: "))

#Guardar en una variable el peso en gramos de cada producto
peso_payaso = 112
peso_muneca = 75

#Calcular el peso total en gramos
peso_total = peso_payaso * cantidad_payasos + peso_muneca * cantidad_munecas

#Imprimir el peso total en gramos (g)
print(f"El peso total es: {peso_total} g")