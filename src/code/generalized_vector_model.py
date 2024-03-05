import itertools
import json
import numpy as np
from math import log
from preprocessing_query import *

with open("corpus.json", "r") as json_file:
    data = json.load(json_file)

filtered_docs = data["corpus"]
weight_doc_matrix = data["vector representation"]
vocabulary = data["vocabulary"]
correlation_matrix = data["correlation_matrix"]

'''def generate_minterm_of_document(doc, processed_query):
    minterms = []

    for term in processed_query:
        if(term in doc):
            minterms.append(1)
        else:
            minterms.append(0)
    return minterms'''

def calculate_similarity(doc_index, processed_query):
    n = len(correlation_matrix[0])
    numerator = 0
    sum_den_i_k = 0
    sum_den_i_q = 0
    weight_query_vector = get_weight_query_vector(processed_query)

    for j in range(0,n):
        for i in range[0:n]:
            w_ik = get_weight_doc(doc_index,i)
            w_jk = get_weight_doc(doc_index, j)
            w_iq = weight_query_vector(i)
            t_i_j = correlation_matrix[i][j]
            numerator = numerator + (w_ik * w_jk * t_i_j)
            sum_den_i_k = sum_den_i_k + (w_ik ** 2)
            sum_den_i_q = sum_den_i_q + (w_iq ** 2)
    
    denominator = np.sqrt(sum_den_i_k) * np.sqrt(sum_den_i_q)

    return numerator / denominator

# TODO: Revisar si es ese el orden de la matriz de pesos
def get_weight_doc(doc_index, term_index):
    return weight_doc_matrix[doc_index][term_index]

def weight_for_query(term, processed_query):
    #Calcular TF
    term_count = processed_query.count(term)
    total_terms = len(processed_query)
    tf = term_count/total_terms
    exp = 1
    #Calcular IDF
    idf = log(exp, 10) + 1
    return tf * idf

def get_weight_query_vector(processed_query):
    weight_query_vector = []
    for term in vocabulary:
        weight_query_vector.append(weight_for_query(term, processed_query))
    return weight_query_vector