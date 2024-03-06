#Solicitar el número de shows musicales que el usuario haya visto en el ultimo año
shows = int(input("¿Cuántos shows musicales ha visto en el último año?: "))

#Obtener un 'true' o 'false' 
respuesta = shows > 3

#Imprimir respuesta
print("¿Ha visto más de 3 shows musicales?:", respuesta)