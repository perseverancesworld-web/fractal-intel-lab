import numpy as np
from scipy.spatial.distance import cosine

class FractalConceptNetwork:
    def __init__(self):
        self.concepts = {}
    
    def add(self, name, vector):
        self.concepts[name] = np.array(vector, dtype=complex)
    
    def match(self, state):
        if not self.concepts:
            return "unknown", 0.0
        similarities = {name: 1 - cosine(state[:len(vec)].real, vec.real) for name, vec in self.concepts.items()}
        best = max(similarities, key=similarities.get)
        return best, similarities[best]