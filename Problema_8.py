#Solicitar la hora en formato HH:MM
hora_actual = input("Ingrese la hora actual (HH:MM): ")

#Separar el str 'hora_actual' en 2 variables str, 'hora' y 'minutos', usando ":" como separador
hora, minutos = hora_actual.split(":")

#Calcular la hora de comer ('hora_comer') convirtiendo los str, 'hora' y 'minutos', en int. 'hora_comer' se convierte en un float
hora_comer = int(hora) + (int(minutos) / 60)

#Según la hora calculada, especificar si es hora de desayunar, almorzar o cenar. Si no es hora de comer, no envíar nada
if 7 <= hora_comer <= 8:
    print("Es hora de desayunar")
elif 12 <= hora_comer <= 13:
    print("Es hora de almorzar")
elif 18 <= hora_comer <= 19:
    print("Es hora de cenar")