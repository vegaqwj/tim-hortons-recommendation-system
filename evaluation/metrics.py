
import numpy as np

def recall_at_k(actual, predicted, k):

    predicted = predicted[:k]

    return len(set(actual) & set(predicted)) / len(actual)

def ndcg_at_k(actual, predicted, k):

    dcg = 0
    for i,p in enumerate(predicted[:k]):
        if p in actual:
            dcg += 1 / np.log2(i+2)

    idcg = sum([1/np.log2(i+2) for i in range(min(len(actual),k))])

    return dcg/idcg if idcg>0 else 0
