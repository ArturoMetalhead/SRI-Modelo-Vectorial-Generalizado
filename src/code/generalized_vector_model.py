import itertools
import json
import numpy as np
from math import log
from preprocessing_query import *
from sklearn.metrics.pairwise import cosine_similarity

'''with open("corpus.json", "r") as json_file:
    data = json.load(json_file)

filtered_docs = data["corpus"]
weight_doc_matrix = data["vector representation"]
vocabulary = data["vocabulary"]
correlation_matrix = data["correlation_matrix"]'''

'''def generate_minterm_of_document(doc, processed_query):
    minterms = []

    for term in processed_query:
        if(term in doc):
            minterms.append(1)
        else:
            minterms.append(0)
    return minterms'''

def calculate_similarity(doc_index,weight_doc_matrix, correlation_matrix, weight_query_vector,n):

    t_i_j=0

    # Calculando el valor de la correlación
    for i in range(0,n):
        for j in range(0,n):
            t_i_j += correlation_matrix[i][j]

    # Escalando el valor de t_i_j
    t_i_j = t_i_j/n

    return cosine_similarity([weight_doc_matrix[doc_index]], [weight_query_vector])[0][0]*t_i_j

def weight_for_query(term, processed_query,n,filtered_docs):

    #Calcular TF

    term_count = processed_query.count(term)
    tf = term_count if term_count > 0 else 0

    #Calcular IDF

    d=0
    for doc in filtered_docs:
        if term in doc:
            d+=1

    if d == 0:
        d=1

    idf = log(n/d)

    return tf * idf

def get_weight_query_vector(processed_query, vocabulary, n,filtered_docs):
    weight_query_vector = []
    for term in vocabulary:
        weight_query_vector.append(weight_for_query(term, processed_query,n,filtered_docs))
    return weight_query_vector