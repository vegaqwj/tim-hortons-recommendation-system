
def recall_at_k(actual, predicted, k):
    predicted = predicted[:k]
    return len(set(predicted) & set(actual)) / len(actual)
