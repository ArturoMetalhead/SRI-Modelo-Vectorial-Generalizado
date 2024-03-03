import itertools
import json

''' def generate_minterms(processed_query):
    with open("corpus.json", "r") as archive: #asumiendo que el json con el corpus se llama corpus
        data = json.load(archive)
    corpus = data["data"["corpus"]] #asumiendo que el dicc se llame data y que la lista del corpus se llame corpus
    vector_rep = data["data"["vector_representation"]] #asumiendo que la lista de pesos se llame vector_representation

    #generar todas las combinaciones de literales
    minterms = []

    for i in range(1, len(processed_query) + 1):
        for comb in itertools.combinations(processed_query, i):
            if len(comb) == 1:
                minterms.append(comb[0])
            else:
                minterm = comb[0]
                for literal in comb[1:]:
                    minterm += " AND " + literal
                minterms.append(minterm)
                '''

def generate_minterm_of_document(doc, processed_query):
    minterms = []

    for term in processed_query:
        if(term in doc):
            minterms.append(1)
        else:
            minterms.append(0)
    return minterms