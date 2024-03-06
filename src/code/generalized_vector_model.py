import numpy as np
from math import log
from src.code.preprocessing_query import *
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(doc_index,weight_doc_matrix, correlation_matrix, weight_query_vector,n):
    """
    Calculate the similarity between a document and a query based on their vector representations,
    correlation matrix, and cosine similarity.

    Args:
        doc_index (int): Index of the document in the weight_doc_matrix to calculate the similarity with.
        weight_doc_matrix (ndarray): Matrix of weighted document vectors.
        correlation_matrix (list): Correlation matrix between terms.
        weight_query_vector (ndarray): Weighted vector representation of the query.
        n (int): Amount of documents.

    Returns:
        float: The similarity score between the document and the query.
    """
    t_i_j=0

    #Calculando el valor de la correlación
    for i in range(0,n):
        for j in range(0,n):
            t_i_j += correlation_matrix[i][j]

    #Escalando el valor de t_i_j
    t_i_j = t_i_j/n
    return cosine_similarity([weight_doc_matrix[doc_index]], [weight_query_vector])[0][0]*t_i_j

def weight_for_query(term, processed_query,n,filtered_docs):
    """
    Calculate the weight of a term in the query based on its term frequency (TF) and inverse document frequency (IDF).

    Args:
        term (str): The term to calculate the weight for.
        processed_query (list): The preprocessed query.
        n (int): The total number of documents in the corpus.
        filtered_docs (list): The list of preprocessed documents.

    Returns:
        float: The weight of the term in the query.
    """
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
    """
    Calculate the weight vector representation of the query based on the processed query, vocabulary,
    total number of documents (n), and list of preprocessed documents (filtered_docs).

    Args:
        processed_query (list): The preprocessed query.
        vocabulary (list): The vocabulary of terms.
        n (int): The total number of documents in the corpus.
        filtered_docs (list): The list of preprocessed documents.

    Returns:
        list: The weight vector representation of the query.
    """
    weight_query_vector = []
    for term in vocabulary:
        weight_query_vector.append(weight_for_query(term, processed_query,n,filtered_docs))
    return weight_query_vector