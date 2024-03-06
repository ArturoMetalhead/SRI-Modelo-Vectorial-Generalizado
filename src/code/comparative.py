
def compare_results(rec_docs_vect,rec_doc_bool,qrls,query_id):
    f_bool=confusion_matrix(rec_doc_bool,qrls,query_id)
    f_vect=confusion_matrix(rec_docs_vect,qrls,query_id)

    print("F-measure for boolean model: ", f_bool)
    print("F-measure for vector model: ", f_vect)


def confusion_matrix(rec_docs,qrls,query_id):
    query_tuples = []
    relevance_metric = 2
    relevants=0
   
    for q in qrls:
        if q[0] == query_id:
            if q[1] < 20:
                query_tuples.append(q)
                if q[2]>=relevance_metric:
                    relevants+=1
    

    relevant_rec ,nrelevant_rec= get_relevant_rec_and_no_relevant_rec(query_tuples, rec_docs, relevance_metric) 
    precision= len(relevant_rec)/len(rec_docs)
    recovered= len(relevant_rec)/(len(rec_docs)+relevants)
    f_pr= 2*precision*recovered/(precision+recovered)

    return f_pr

def get_relevant_rec_and_no_relevant_rec(query_tuples, rec_docs, relevance_metric):
    relevant_rec = set()
    no_relevant_rec = set()

    for doc_tuple in rec_docs:
        doc_index = doc_tuple[1]
        for q in query_tuples:
            if q[1] == doc_index:
                if q[2] >= relevance_metric:
                    relevant_rec.add(doc_index)
                else:
                    no_relevant_rec.add(doc_index)
    return relevant_rec, no_relevant_rec



