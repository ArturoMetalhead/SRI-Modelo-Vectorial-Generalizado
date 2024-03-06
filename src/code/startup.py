from preprocessing_query import *
from generalized_vector_model import *
import json
from boolean_model import *

print("Bienvenido al motor de búsqueda de documentos")

def start():
    with open("corpus.json", "r") as json_file:
        data = json.load(json_file)

    docs = data["original_corpus"]
    filtered_docs = data["corpus"]
    weight_doc_matrix = data["vector representation"]
    vocabulary = data["vocabulary"]
    correlation_matrix = data["correlation_matrix"]

    query = ""
    while(True):
        print("Ingrese la consulta deseada en inglés")
        query = input("Buscar:")
        if query == "b":
            break

        else:
            print(execute_model(query, filtered_docs, weight_doc_matrix, vocabulary, correlation_matrix, docs))
            print(model_bool(filtered_docs, query))

def execute_model(query, filtered_docs, weight_doc_matrix, vocabulary, correlation_matrix, docs):
    processed_query = preprocess_query(query)
    similarity = []

    n = len(correlation_matrix[0]) #Cantidad de documentos
    weight_query_vector = get_weight_query_vector(processed_query, vocabulary,n,filtered_docs)

    for i in range(0, len(filtered_docs)):
        similarity.append(calculate_similarity(i, weight_doc_matrix, correlation_matrix,weight_query_vector,n))
    return define_ranking(similarity, docs)
    
def define_ranking(similarity, docs):
    ranking = []
    for i in range(0, len(similarity)):
        if similarity[i] >= 1:
            ranking.append((similarity[i],i, docs[i]))
    ranking.sort(reverse=True)
    return ranking

start() 