from src.code.preprocessing_functions import *

def preprocess_query(query):
    """
    Preprocess a query by tokenizing, cleaning, removing stopwords, reducing morphological forms,
    filtering tokens by occurrence, and building a vocabulary.

    Args:
        query (str): The input query to be preprocessed.

    Returns:
        list: A list of tokens representing the vocabulary after preprocessing the query.
    """
    tokenized_query = tokenization([query])
    cleaned_query = remove_noise(tokenized_query)
    no_stop_words_query = remove_stopwords(cleaned_query)
    reduced_query = morphological_reduction(no_stop_words_query)
    filtered_query, dictionary = filter_tokens_by_occurrence(reduced_query)
    vocabulary = build_vocabulary(dictionary)
    return vocabulary

    