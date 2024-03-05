from preprocessing_functions import *

def preprocess_query(query):
    tokenized_query = tokenization([query])
    cleaned_query = remove_noise(tokenized_query)
    no_stop_words_query = remove_stopwords(cleaned_query)
    reduced_query = morphological_reduction(no_stop_words_query)
    filtered_query, dictionary = filter_tokens_by_occurrence(reduced_query)
    vocabulary = build_vocabulary(dictionary)
    return filtered_query

    