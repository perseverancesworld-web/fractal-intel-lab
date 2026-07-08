import numpy as np

def compute_stability(state):
    return 1.0 - np.std(np.abs(state))

def compute_coherence(state):
    return np.mean(np.abs(state))

def compute_entropy(state):
    # Simplified
    return -np.sum(state * np.log(np.abs(state) + 1e-10))

def run_metrics(state):
    return {
        "stability": compute_stability(state),
        "coherence": compute_coherence(state),
        "entropy": compute_entropy(state)
    }