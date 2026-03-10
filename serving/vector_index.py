
from sklearn.neighbors import NearestNeighbors

class VectorIndex:

    def __init__(self, embeddings):
        self.index = NearestNeighbors(n_neighbors=10)
        self.index.fit(embeddings)

    def search(self, query):
        dist, idx = self.index.kneighbors([query])
        return idx
