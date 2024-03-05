import ir_datasets
import nltk
import spacy
import gensim
import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np

##Cargando el corpus

#dataset = ir_datasets.load("" ) #insertar aqui los documentos
#documents = [doc.text for doc in dataset.docs_iter()]

##Tokenizacion

#tokenized_docs = []
#vector_repr = []
#dictionary = {}
#vocabulary = []

#nlp = spacy.load("en_core_web_sm")
def tokenization(documents):
    nlp = spacy.load("en_core_web_sm")
    return [[token for token in nlp(doc)] for doc in documents]

#tokenization(documents)

##Eliminacion de ruido

def remove_noise(tokenized_docs):
    return [[token for token in doc if token.is_alpha] for doc in tokenized_docs]

#remove_noise(tokenization(documents))

##Eliminacion de Stop-Words

def remove_stopwords(tokenized_docs):
    stopwords = spacy.lang.en.stop_words.STOP_WORDS
    return [
        [token for token in doc if token.text not in stopwords] for doc in tokenized_docs
    ]

#remove_stopwords(remove_noise(tokenization(documents)))

##Reduccion Morfologica

def morphological_reduction(tokenized_docs, use_lemmatization=True):
    stemmer = nltk.stem.PorterStemmer()
    return [
        [token.lemma_ if use_lemmatization else stemmer.stem(token.text) for token in doc]
        for doc in tokenized_docs
    ]

#morphological_reduction(remove_stopwords(remove_noise(tokenization(documents))), True)

##Filtrado segun ocurrencia

def filter_tokens_by_occurrence(tokenized_docs, no_below=1, no_above=20):
    #global dictionary
    dictionary = {}
    dictionary = gensim.corpora.Dictionary(tokenized_docs)
    dictionary.filter_extremes(no_below=no_below, no_above=no_above)

    filtered_words = [word for _, word in dictionary.iteritems()]
    filtered_tokens = [
        [word for word in doc if word in filtered_words]
        for doc in tokenized_docs
    ]

    return filtered_tokens, dictionary

#tokenized_docs = filter_tokens_by_occurrence(tokenized_docs)

##Construccion del vocabulario

def build_vocabulary(dictionary):
    vocabulary = list(dictionary.token2id.keys())
    return vocabulary

#vocabulary = build_vocabulary(dictionary)

#region implemetar
##Representacion Vectorial  (Me parece que esta es la parte que uno debe implementar)

# Modificado para usar tfidf por defecto
def vector_representation(tokenized_docs, dictionary, use_bow=True):
    corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]
    ttfidf = gensim.models.TfidfModel(corpus)
    vector_repr = [ttfidf[doc] for doc in corpus]

    return vector_repr

#vector_repr = vector_representation(tokenized_docs, dictionary, vector_repr)

##Etiquetado de las partes del discurso

def pos_tagger(tokenized_docs):
    return [
        [(token.text, token.tag_) for token in doc]
        for doc in tokenized_docs
    ]

#pos_tags = pos_tagger(tokenization(documents))

#Representar los documentos en forma de vector binario en dependencia de los términos que aparecen
def docs_vectorial_rep(vocabulary, filtered_tokens):
    vectorial_docs = []
    for doc in filtered_tokens:
        doc_rep = []
        for voc in vocabulary:
            if voc in doc:
                doc_rep.append(1)
            else: 
                doc_rep.append(0)
        vectorial_docs.append(doc_rep)
    return vectorial_docs

#Obtener la frecuencia de aparicion de un termino i en un documento k
def get_c(doc, term):
    c = 0
    for token in doc:
        if token == term:
            c = c + 1
    return c
    

def get_correlation_between_terms(vectorial_docs, term_i, term_j):
    df = pd.DataFrame(vectorial_docs)
    filtered_df = df[[term_i, term_j]]
    contingency_table = pd.crosstab(filtered_df[term_i], filtered_df[term_j])
    observed = contingency_table.values
    chi2, _, _, expected = chi2_contingency(observed)    
    phi = np.sqrt(chi2 / np.sum(observed))
    return phi

def get_correlation_matrix(vectorial_docs):
    correlation_matrix = []
    for i in range(len(vectorial_docs[0])):
        doc_correlation = []
        for j in range(len(vectorial_docs[0])):
            doc_correlation.append(get_correlation_between_terms(vectorial_docs, i, j))
        correlation_matrix.append(doc_correlation)
    return correlation_matrix
#endregion