import numpy as np

class OneiricEngine:
    """Offline replay and consolidation (dreaming)."""
    def __init__(self, memory_size=1000):
        self.memory = []
        self.memory_size = memory_size
    
    def replay(self, experiences):
        """Consolidate memories."""
        self.memory.extend(experiences)
        if len(self.memory) > self.memory_size:
            self.memory = self.memory[-self.memory_size:]
        # Simple consolidation: average attractors
        if self.memory:
            return np.mean([np.array(exp) for exp in self.memory], axis=0)
        return None
    
    def dream(self):
        """Generate synthetic replay."""
        if not self.memory:
            return None
        return np.random.choice(self.memory, size=min(5, len(self.memory)))