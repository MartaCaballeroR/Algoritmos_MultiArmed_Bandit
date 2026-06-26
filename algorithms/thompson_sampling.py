import numpy as np
from base.initial import Initial

class ThompsonSampling:
    def __init__(self, n_slots, gate_names):
        self.n_slots = n_slots
        self.gate_names = gate_names
        self.alpha = Initial.initial_alpha(n_slots, gate_names)
        self.beta = Initial.initial_beta(n_slots, gate_names)

    def choose_action(self):
        combination = []
        for i in range(self.n_slots):
            sampled_values = {}
            for gate in self.gate_names:
                sampled_values[gate] = np.random.beta(self.alpha[i][gate], self.beta[i][gate])
            best_gate = max(sampled_values, key=sampled_values.get)
            combination.append(best_gate)
        return combination
    
    def update(self, combination, reward):
        for i, gate in enumerate(combination):
            if reward == 1:
                self.alpha[i][gate] += reward
            else:
                self.beta[i][gate] += (1 - reward)

    def best_combination(self):
        best_combination = []
        for i in range(self.n_slots):
            expected_values = {
                gate: self.alpha[i][gate] / (self.alpha[i][gate] + self.beta[i][gate]) 
                for gate in self.gate_names
            }
            best_combination.append(max(expected_values, key=expected_values.get))
        return best_combination 