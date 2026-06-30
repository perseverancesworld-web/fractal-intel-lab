import numpy as np
from .fbits import Fbit
from .homeostasis import Homeostasis
from .oneiric import OneiricEngine
from .concepts import FractalConceptNetwork

class FractalChain:
    def __init__(self, fbits):
        self.fbits = fbits
    
    def process(self, signal):
        for fbit in self.fbits:
            signal = fbit.iterate(signal)
        return signal

class FractalMind:
    def __init__(self, chains=None, concept_net=None):
        self.chains = chains or []
        self.concept_net = concept_net or FractalConceptNetwork()
        self.homeostasis = Homeostasis()
        self.oneiric = OneiricEngine()
    
    def think_features(self, transducer, raw_vec):
        signal = transducer.transduce(raw_vec)
        state = self.chains[0].process(signal) if self.chains else signal
        state = self.homeostasis.regulate(state)
        concept_name, confidence = self.concept_net.match(state)
        # Dream consolidation example
        self.oneiric.replay([state])
        return signal, state, concept_name, confidence

class FractalTransducer:
    def __init__(self, feature_dim=128):
        self.feature_dim = feature_dim
    
    def transduce(self, raw_vec):
        # Map real-world vector to complex plane
        cvec = raw_vec.astype(complex)
        if len(cvec) > self.feature_dim:
            cvec = cvec[:self.feature_dim]
        else:
            cvec = np.pad(cvec, (0, self.feature_dim - len(cvec)))
        return cvec