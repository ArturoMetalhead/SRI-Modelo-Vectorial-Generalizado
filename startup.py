from src.code.preprocessing_query import *
from src.code.generalized_vector_model import *
import json
from src.code.boolean_model import *

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
            #print(model_bool(filtered_docs, query))

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

######

def compare_models():
    with open("corpus.json", "r") as json_file:
        data = json.load(json_file)

    docs = data["original_corpus"]
    filtered_docs = data["corpus"]
    weight_doc_matrix = data["vector representation"]
    vocabulary = data["vocabulary"]
    correlation_matrix = data["correlation_matrix"]

    # Escogiendo la primera query

    query = data["queries"][8]

    results_vect=execute_model(query, filtered_docs, weight_doc_matrix, vocabulary, correlation_matrix, docs)

    results_bool=model_bool(filtered_docs, query)

    qrls = data["qrels"]
    compare_results(results_vect,results_bool,qrls,0)



def compare_results(rec_docs_vect,rec_doc_bool,qrls,query_id):
    f_bool=confusion_matrix(rec_doc_bool,qrls,query_id)
    f_vect=confusion_matrix(rec_docs_vect,qrls,query_id)

    print("F-measure for boolean model: ", f_bool)
    print("F-measure for vector model: ", f_vect)


def confusion_matrix(rec_docs,qrls,query_id):
    query_tuples = []
    relevance_metric = 1
    relevants=0
   
    for q in qrls:
        if q[0] == query_id:
            if int(q[1]) < 20:
                query_tuples.append(q)
                if q[2]>=relevance_metric:
                    relevants+=1
    

    relevant_rec ,nrelevant_rec= get_relevant_rec_and_no_relevant_rec(query_tuples, rec_docs, relevance_metric) 
    if(len(rec_docs)==0):
        precision= 0
    else:
        precision= len(relevant_rec)/len(rec_docs)
    
    if(relevants==0):
        recovered= 0
    else:
        recovered= len(relevant_rec)/relevants
    if(precision+recovered==0):
        f_pr= 0
    else:
        f_pr= 2*precision*recovered/(precision+recovered)

    return f_pr

def get_relevant_rec_and_no_relevant_rec(query_tuples, rec_docs, relevance_metric):
    relevant_rec = set()
    no_relevant_rec = set()

    for doc_tuple in rec_docs:
        doc_index = doc_tuple[1]
        for q in query_tuples:
            if q[1] == doc_index:
                if q[2] >= relevance_metric:
                    relevant_rec.add(doc_index)
                else:
                    no_relevant_rec.add(doc_index)
    return relevant_rec, no_relevant_rec


#compare_models()