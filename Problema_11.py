#Guardar la lista original en una variable e imprimirla
lista = [1, 1, 2, 3, 4, 4, 5, 1]
print(f"Lista original: {lista}")

#Convertir la lista original en un conjunto para eliminar los duplicados y convertirlo nuevamente en una lista e imprimir la lista resultante
lista = list(set(lista))
print(f"Lista resultante: {lista}")