import os
from preprocessing import *
from boolean_model import *

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

print(start(preprocess(lista_archivos)))

#consulta:(dog and hunter) or (cat and not human) or (dog and not cat)