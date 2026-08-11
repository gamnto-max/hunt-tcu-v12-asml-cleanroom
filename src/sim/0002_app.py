import numpy as np
class QuantumStreamGenerator:
    def __init__(self):
        self.scale = 256
    def generate_vectors(self):
        signals = [1.25, -2.50, 3.125]
        noises = [0.45, -0.85, 1.15]
        print('Signals:', signals)
        print('Noises:', noises)
if __name__ == '__main__':
    print('--- INICIANDO 0002_APP.PY ---')
    g = QuantumStreamGenerator()
    g.generate_vectors()