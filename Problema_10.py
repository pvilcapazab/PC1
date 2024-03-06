#Guardar la lista de muestra en una variable e imprimir la lista para verla
lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
print(f"Lista de muestra: {lista}")

#Eliminar la posición 5, 4, y 0 de mayor a menor para que no altere la posición de los valores
lista.remove(lista[5])
lista.remove(lista[4])
lista.remove(lista[0])

#Imprimir la lista resultante
print(f"Lista resultante: {lista}")