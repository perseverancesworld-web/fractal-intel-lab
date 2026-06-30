import numpy as np

class Fbit:
    """Stateful fractal cell."""
    def __init__(self, mode="mandelbrot", params=None, depth=100):
        self.mode = mode
        self.params = params or {}
        self.depth = depth
        self.state = np.zeros(8, dtype=complex)
        
    def iterate(self, input_signal):
        """Apply fractal iteration."""
        if self.mode == "mandelbrot":
            z = input_signal + 0.1j if np.isscalar(input_signal) else input_signal
            for _ in range(min(self.depth, 20)):  # Limit for speed
                z = z**2 + 0.1
            return z
        return input_signal

    def get_state(self):
        return self.state