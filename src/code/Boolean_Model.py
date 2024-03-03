from sympy import sympify, to_dnf, Not, And, Or

def convert_to_logic(query,nlp):
    
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

def query_to_dnf(query,nlp):

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


#######REVISAR

corpus=[["A","B","C"],["A","B"],["A","C"],["A","B","D"],["A","B","C","D"],["A","B" ]]

def get_matching_docs(query_dnf,corpus):

    setDnf = set()

    for term in query_dnf.args:
        
        if isinstance(term, Or):
            terms=[]
            for subterm in term.args:
                if isinstance(subterm, Not):
                    terms.append(not_term_in_docs(subterm.args[0],corpus))
                else:
                    terms.append(term_in_docs(subterm,corpus))
            
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
                    terms.append(not_term_in_docs(subterm.args[0],corpus))
                else:
                    terms.append(term_in_docs(subterm,corpus))

            setTemp = set()
            setTemp.add(terms[0])
            for i in terms:
                setTemp = setTemp & i

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
    

def not_term_in_docs(term,corpus):
    sets=set()
    for doc in corpus:
        if term in doc:
            sets.add(doc)
    return sets

    # sets=set()
    # sets.add("s1")
    # return sets

def term_in_docs(term,corpus):
    sets=set()
    for doc in corpus:
        if term not in doc:
            sets.add(doc)
    return sets

    # sets=set()
    # sets.add("s2")
    # return sets

query = "A AND (B OR NOT C)"     # insertar consulta
#query="A | B | C"
get_matching_docs(query_to_dnf(query),corpus)