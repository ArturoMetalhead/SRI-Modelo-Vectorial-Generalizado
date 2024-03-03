import gensim
import spacy
from sympy import sympify, to_dnf, Not, And, Or

nlp = spacy.load("en_core_web_sm")

def query_to_dnf(query):

    processed_query = ""
    
    # Tokenizar la consulta
    query_tokens = nlp(query)
    
    # Reemplazar los operadores lógicos por sus equivalentes en sympy
    processed_query=query_tokens.text
    processed_query = processed_query.replace("AND", "&").replace("OR", "|").replace("NOT", "~")
    
    # Convertir a expresión sympy y aplicar to_dnf
    query_expr = sympify(processed_query, evaluate=False)
    query_dnf = to_dnf(query_expr, simplify=True)

    return query_dnf

# consulta = "A AND (B OR NOT C)"
# consulta_dnf = query_to_dnf(consulta)


def convert_to_logic(query):
    
    # Tokenizar la consulta
    doc = nlp(query)
    
    # Lista para almacenar los términos clave
    terms = []
    
    # Recorrer los tokens de la consulta
    for token in doc:
        # Verificar si el token es un sustantivo o un adjetivo
        if token.pos_ in ['NOUN', 'ADJ']:
            terms.append(token.text)
        elif token.text == 'and':
            terms.append('AND')
        elif token.text == 'or':
            terms.append('OR')
        elif token.text == 'not':
            terms.append('NOT')

    # Construir la expresión lógica
    logic_expr = ' '.join(terms)

    return logic_expr

# Ejemplo de uso
# consulta = "I have a cat and a dog"
# expresion_logica = convert_to_logic(consulta)


#######REVISAR

# tokenized_docs = []     # cargar del json o del corpus procesado
# dictionary = gensim.corpora.Dictionary(tokenized_docs)
# vocabulary = list(dictionary.token2id.keys())
# corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]

# def get_matching_docs(query_dnf):
#     global tokenized_docs, dictionary, corpus, vocabulary

#     matching_documents = []
#     for term in query_dnf.args:
#         if isinstance(term, Not):
#             term = term.args[0]
#             term = term.args[0] if isinstance(term, Not) else Not(term)
#         term = term.args[0] if isinstance(term, Not) else term

#         if isinstance(term, Or):
#             matching_documents.extend(get_matching_docs(term))
#         elif isinstance(term, And):  # Agregar verificación para términos de tipo And
#             term_docs = None
#             for subterm in term.args:
#                 subterm = subterm.args[0] if isinstance(subterm, Not) else subterm
#                 subterm = str(subterm).lower()
#                 if subterm in vocabulary:
#                     subterm_id = dictionary.token2id[subterm]
#                     subterm_docs = [doc for doc in corpus if subterm_id in dict(doc)]
#                     if term_docs is None:
#                         term_docs = set(subterm_docs)
#                     else:
#                         term_docs = term_docs.intersection(subterm_docs)
#             if term_docs is not None:
#                 matching_documents.extend(list(term_docs))
#         else:
#             term = term.args[0] if isinstance(term, Not) else term
#             term = str(term).lower()  # Convertir el término en una cadena y aplicar lower()
#             if term in vocabulary:
#                 term_id = dictionary.token2id[term]
#                 term_docs = [doc for doc in corpus if term_id in dict(doc)]
#                 matching_documents.extend(term_docs)

#     return matching_documents

# query = "(A & B) | (A | ~C)"     # insertar consulta
# get_matching_docs(query_to_dnf(query))