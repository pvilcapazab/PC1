#Solicitar consumo y %propina
consumo = float(input("Ingrese el total de su consumo: S/"))
propina_porcentaje = float(input("Ingrese el porcentaje de propina que desea dejar: "))

#Calcular la propina a dejar
propina = consumo * (propina_porcentaje / 100)

#Imprimir la propina a dejar
print(f"La propina que debe dejar es: S/{propina}")