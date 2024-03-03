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

tokenized_docs = []     # cargar del json o del corpus procesado
dictionary = gensim.corpora.Dictionary(tokenized_docs)
vocabulary = list(dictionary.token2id.keys())
corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]

def get_matching_docs(query_dnf):
    global tokenized_docs, dictionary, corpus, vocabulary

    #matching_documents = []#Meter aqui los documentos que coinciden con el primer termino de la consulta,los que coinciden con el segundo y asi
    setDnf = set()

    # for match in matching_documents:
    #     setDnf.add(match)

    for term in query_dnf.args:
        
        if isinstance(term, Or):
            terms=[]
            for subterm in term.args:
                if isinstance(subterm, Not):
                    terms.append(not_term_in_docs(subterm.args[0]))
                else:
                    terms.append(term_in_docs(subterm))
            
            setTemp = set()
            for i in terms:
                setTemp = setTemp | i

            setDnf.add(setTemp)
            # term1 = {str(term1).lower()}
            # term2 = {str(term2).lower()}
           
        elif isinstance(term, And):
            
            terms=[]
            for subterm in term.args:
                if isinstance(subterm, Not):
                    terms.append(not_term_in_docs(subterm.args[0]))##recordar devolver los documentos en sets
                else:
                    terms.append(term_in_docs(subterm))

            setTemp = set()
            for i in terms:
                setTemp = setTemp & i #cambiar para que no le haga & con un 0

            setDnf.add(setTemp)#annadir un set dentro del set

            
            # term1 = {str(term1).lower()}
            # term2 = {str(term2).lower()}

        elif isinstance(term, Not):
            term=not_term_in_docs(term.args[0])
            setDnf.add(term)

        else:
            term=term_in_docs(term)
            setDnf.add(term)

    return setDnf
    

def not_term_in_docs(term):
    sets=set()
    sets.add("s1")
    return sets

def term_in_docs(term):
    sets=set()
    sets.add("s2")
    return sets

query = "A AND (B OR NOT C)"     # insertar consulta
#query="A | B | C"
get_matching_docs(query_to_dnf(query))