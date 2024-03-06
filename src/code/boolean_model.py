import preprocessing
from boolean_model_functions import *
import spacy


def start(corpus):

    #Implementar el preprocesamiento de los documentos

    #Leer de la terminal la consulta
    query = input("Ingrese la consulta: ")

    #Preprocesar la consulta
    nlp = spacy.load("en_core_web_sm")

    query = convert_to_logic(query, nlp)
    query = query_to_dnf(query, nlp)

    #Realizar la consulta
    matching_documents = get_matching_docs(query,corpus)

    print(matching_documents)