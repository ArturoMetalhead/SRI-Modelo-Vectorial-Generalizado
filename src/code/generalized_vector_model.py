import itertools
import json
import numpy as np
from math import log
from preprocessing_query import *

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

def calculate_similarity(doc_index, processed_query, weight_doc_matrix, correlation_matrix, vocabulary):
    n = len(correlation_matrix[0])
    numerator = 0
    sum_den_i_k = 0
    sum_den_i_q = 0
    weight_query_vector = get_weight_query_vector(processed_query, vocabulary)

    for j in range(0,n):
        for i in range(0,n):
            w_ik = weight_doc_matrix[doc_index][i]
            w_jq = weight_query_vector[j]
            #w_iq = weight_query_vector[i]
            #t_i_j = correlation_matrix[i][j]
            #numerator = numerator + (w_ik * w_jk * t_i_j)

            numerator = numerator + (w_ik * w_jq)
            
    for i in range(0,n):
        wd_ik = weight_doc_matrix[doc_index][i]
        wd_iq = weight_query_vector[i]
        sum_den_i_k = sum_den_i_k + (wd_ik ** 2)
        sum_den_i_q = sum_den_i_q + (wd_iq ** 2)

    denominator = np.sqrt(sum_den_i_k) * np.sqrt(sum_den_i_q)

    return numerator / denominator

def weight_for_query(term, processed_query):
    #Calcular TF
    term_count = processed_query.count(term)
    total_terms = len(processed_query)
    tf = (1 + log(term_count, 2)) if term_count > 0 else 0
    exp = 1
    #Calcular IDF
    idf = log(exp, 2) + 9
    return tf * idf

def get_weight_query_vector(processed_query, vocabulary):
    weight_query_vector = []
    for term in vocabulary:
        weight_query_vector.append(weight_for_query(term, processed_query))
    return weight_query_vector