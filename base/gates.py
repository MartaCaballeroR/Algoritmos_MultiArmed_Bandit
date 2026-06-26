# Imports
import numpy as np

class Gates:
    def __init__(self):
        self._gates = {
            "AND":  np.array([0, 0, 0, 1]),
            "OR":   np.array([0, 1, 1, 1]),
            "NAND": np.array([1, 1, 1, 0]),
            "XOR":  np.array([0, 1, 1, 0])
        }

    # Propiedad para extraer los nombres de las puertas
    @property
    def names(self):
        return list(self._gates.keys())


    # Calculo de la salida basado en indice
    def evaluate(self, gate, input_a, input_b):

        if gate not in self._gates:
            raise ValueError(f"Puerta '{gate}' no reconocida.")
        
        index = 2 * int(input_a) + int(input_b)
        return self._gates[gate][index]