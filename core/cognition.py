import numpy as np
from .fbits import Fbit

class FractalChain:
    def __init__(self, fbits):
        self.fbits = fbits
    
    def process(self, signal):
        for fbit in self.fbits:
            signal = fbit.iterate(signal)
        return signal

class FractalMind:
    def __init__(self, chains, concept_net):
        self.chains = chains
        self.concept_net = concept_net
    
    def think_features(self, transducer, raw_vec):
        signal = transducer.transduce(raw_vec)
        state = self.chains[0].process(signal) if self.chains else signal
        concept_name, confidence = self.concept_net.match(state)
        return signal, state, concept_name, confidence

class FractalTransducer:
    def __init__(self, feature_dim=128):
        self.feature_dim = feature_dim
    
    def transduce(self, raw_vec):
        # Map to complex plane
        return raw_vec.astype(complex)[:self.feature_dim] if len(raw_vec) > self.feature_dim else np.pad(raw_vec.astype(complex), (0, self.feature_dim - len(raw_vec)))