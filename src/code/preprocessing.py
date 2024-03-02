import ir_datasets
import nltk
import spacy
import gensim
import json
from preprocessing_functions import *

#Corpus
# TODO: cargar documentos
#dataset = ir_datasets.load("" ) 

# TODO: Cargar documentos a la hora de iniciar, pues se debe pasar a preprocess ya el corpus deseado.

#documents = [doc.text for doc in dataset.docs_iter()]

def preprocess(documents):
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
    # TODO: Determinar si lo dejamos solo con Tfidf
    vector_rep = vector_representation(filtered_docs, dictionary)

    #Etiquetar
    # TODO: Verificar para que es el tagger y determinar si se le pasa el primer tokenized_docs o filtered_docs
    tagged_docs = pos_tagger(tokenized_docs)

    # TODO: Guardar esto en el json (?)
    #Guardar documento preprocesado en el json
    with open("corpus.json", "w") as json_file:
        json.dump(vector_rep, json_file)