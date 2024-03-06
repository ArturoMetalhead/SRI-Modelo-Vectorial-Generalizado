import ir_datasets
import nltk
import spacy
import gensim
import json
from preprocessing_functions import *


def load_dataset():
    """
    Load the dataset from the "ir_datasets" library.

    Returns:
        ir_datasets.Dataset: The dataset.
    """
    dataset = ir_datasets.load("cranfield")

    documents = []
    queries = []
    qrels = []

    for i, doc in enumerate(dataset.docs_iter()):
        if i >= 20:
            break
        documents.append(doc.text)
    
    for i, query in enumerate(dataset.queries_iter()):
        if i >= 20:
            break
        queries.append(query.text)

    for i, qrel in enumerate(dataset.qrels_iter()):
        qrels.append(qrel)

    # documents = [doc.text for doc in dataset.docs_iter()]
    # queries = [query.text for query in dataset.queries_iter()]
    # qrels = [qrel for qrel in dataset.qrels_iter()]
    
    return documents, queries, qrels

def preprocess(documents, queries, qrels):
    """
    Preprocess a list of documents by performing tokenization, noise removal, stopword removal,
    morphological reduction, filtering by occurrence, building a vocabulary, vector representation,
    part-of-speech tagging, calculating correlation matrix, and saving the preprocessed data to a JSON file.

    Args:
        documents (list): A list of documents to be preprocessed.

    Returns:
        None
    """
    #Tokenizar documentos
    tokenized_docs = tokenization(documents) 

    #Eliminar ruido
    cleaned_docs = remove_noise(tokenized_docs)

    #Eliminar Stop-words
    no_stop_words_docs = remove_stopwords(cleaned_docs)

    #Reducir Morfológicamente
    reduced_docs = morphological_reduction(no_stop_words_docs)

    #Filtrar por ocurrencia
    filtered_docs, dictionary = filter_tokens_by_occurrence(reduced_docs)

    #Construir Vocabulario
    vocabulary = build_vocabulary(dictionary)

    #Representar Vectorialmente
    vector_rep = vector_representation(filtered_docs, vocabulary)

    #Etiquetar
    tagged_docs = pos_tagger(tokenized_docs)

    vectorial_docs = docs_vectorial_rep(vocabulary, filtered_docs)

    correlation_matrix = get_correlation_matrix(vectorial_docs)

    #Guardar documento preprocesado en el json
    data = {"original_corpus": documents,
            "queries": queries,
            "qrels": qrels,
            "corpus": filtered_docs,
            "vector representation": vector_rep,
            "vocabulary" : vocabulary,
            "correlation_matrix": correlation_matrix}
    with open("corpus.json", "w") as json_file:
        json.dump(data, json_file)

documents, queries, qrels = load_dataset()
preprocess(documents, queries, qrels)
