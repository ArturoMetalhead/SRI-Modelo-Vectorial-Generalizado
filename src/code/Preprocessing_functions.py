import ir_datasets
import nltk
import spacy
import gensim

##Cargando el corpus

#dataset = ir_datasets.load("" ) #insertar aqui los documentos
#documents = [doc.text for doc in dataset.docs_iter()]

##Tokenizacion

#tokenized_docs = []
#vector_repr = []
#dictionary = {}
#vocabulary = []

nlp = spacy.load("en_core_web_sm")
def tokenization(documents):
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

def filter_tokens_by_occurrence(tokenized_docs, no_below=5, no_above=0.5):
    global dictionary
    dictionary = gensim.corpora.Dictionary(tokenized_docs)
    dictionary.filter_extremes(no_below=no_below, no_above=no_above)

    filtered_words = [word for _, word in dictionary.iteritems()]
    filtered_tokens = [
        [word for word in doc if word in filtered_words]
        for doc in tokenized_docs
    ]

    return filtered_tokens

#tokenized_docs = filter_tokens_by_occurrence(tokenized_docs)

##Construccion del vocabulario

def build_vocabulary(dictionary):
    vocabulary = list(dictionary.token2id.keys())
    return vocabulary

#vocabulary = build_vocabulary(dictionary)

#region implemetar
##Representacion Vectorial  (Me parece que esta es la parte que uno debe implementar)

# Modificado para usar tfidf por defecto
def vector_representation(tokenized_docs, dictionary, vector_repr, use_bow=True):
    corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]

    """if use_bow:
        vector_repr = corpus
    else:
        tfidf = gensim.models.TfidfModel(corpus)
        vector_repr = [tfidf[doc] for doc in corpus] """
    
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

#endregion