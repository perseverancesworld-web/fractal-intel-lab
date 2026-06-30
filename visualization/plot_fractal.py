import numpy as np
import matplotlib.pyplot as plt
from core.fbits import Fbit

def plot_fractal_state(fbit, title="Fractal State"):
    # Placeholder visualization
    state = fbit.get_state()
    plt.figure()
    plt.plot(np.real(state), np.imag(state), 'o-')
    plt.title(title)
    plt.xlabel('Real')
    plt.ylabel('Imag')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    fbit = Fbit()
    plot_fractal_state(fbit)