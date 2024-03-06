from boolean_model_functions import *
import spacy


def model_bool(corpus, query):

    #Preprocesar la consulta
    nlp = spacy.load("en_core_web_sm")

    query = convert_to_logic(query, nlp)
    query = query_to_dnf(query, nlp)

    #Realizar la consulta
    matching_documents = get_matching_docs(query,corpus)

    results=[]

    # Convertir matching_documents a lista
    matching_documents = list(matching_documents)

    for i in range(0, len(matching_documents)):
        results.append((1,matching_documents[i]))

    return results