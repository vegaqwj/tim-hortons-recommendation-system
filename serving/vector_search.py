
from sklearn.neighbors import NearestNeighbors
import numpy as np

class VectorSearch:

    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.index = NearestNeighbors(n_neighbors=10, metric="cosine")
        self.index.fit(embeddings)

    def search(self, query_vector):
        distances, indices = self.index.kneighbors([query_vector])
        return indices[0]
