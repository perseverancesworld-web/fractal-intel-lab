from core.fbits import Fbit
from core.cognition import FractalChain, FractalMind
from core.transducer import FractalTransducer
from core.concepts import FractalConceptNetwork
import numpy as np

fbits = [
    Fbit(mode="mandelbrot", params={}, depth=100),
    Fbit(mode="julia", params={"c": complex(-0.7, 0.27)}, depth=100),
]

chain = FractalChain(fbits)

concept_net = FractalConceptNetwork()
concept_net.add("coherence", vector=[1.0] * 8)
concept_net.add("tension", vector=[(-1) ** i for i in range(8)])

mind = FractalMind(chains=[chain], concept_net=concept_net)
transducer = FractalTransducer(feature_dim=128)

raw_vec = np.random.randn(128)
signal, state, concept_name, confidence = mind.think_features(transducer, raw_vec)

print("Signal:", signal)
print("Concept:", concept_name, "confidence:", confidence)