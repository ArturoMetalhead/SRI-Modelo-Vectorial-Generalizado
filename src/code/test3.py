import os
from preprocessing import *

archivos = os.listdir("./src/code")


# Crear una lista vacía
lista_archivos = []

# Recorrer la lista de nombres de archivos
for archivo in archivos:
    # Si el archivo es un archivo TXT
    if archivo.endswith(".txt"):
        pathh="./src/code/"+archivo
        # Abrir el archivo en modo lectura
        with open(pathh, "r") as f:
            # Agregar el contenido del archivo a la lista
            lista_archivos.append(f.read())

# Imprimir la lista
print(lista_archivos)

preprocess(lista_archivos)