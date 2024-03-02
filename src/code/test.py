import os
from preprocessing import *

archivos = os.listdir("./src/code")

# Crear una lista vacía
lista = []

# Recorrer la lista de archivos
for archivo in archivos:
    # Si el archivo es un archivo TXT
    if archivo.endswith(".txt"):
        # Agregar el nombre del archivo a la lista
        lista.append(archivo)

preprocess(lista)

