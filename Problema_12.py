#Guardar en una variable el diccionario donde guardan lo diferentes formatos de archivos
lista = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

#Solicitar al usuario que ingrese el nombre y formato de su archivo
archivo = input("Ingrese el nombre y formato de su archivo (ejemplo.png): ").lower()

#Separar el nombre y formato del archivo
nombre, formato = archivo.split(".")

#Verificar si el formato está en el diccionario
if f".{formato}" in lista:
    #Imprimir el tipo MIME si está en el diccionario
    print(lista[f".{formato}"])
else:
    print("application/octet-stream")