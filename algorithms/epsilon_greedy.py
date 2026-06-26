import random
import numpy as np
from base.initial import Initial

class EpsilonGreedy:
    def __init__(self, n_slots, gate_names, epsilon=0.1):
        self.n_slots = n_slots
        self.gate_names = gate_names
        self.epsilon = epsilon
        
        self.q_values = Initial.initial_q_values(n_slots, gate_names)
        self.counts = Initial.initial_counts(n_slots, gate_names)

    def choose_action(self):
        combination = []
        for i in range(self.n_slots):
            if random.random() < self.epsilon:
                action = random.choice(self.gate_names)
            else:
                action = max(self.q_values[i], key=self.q_values[i].get)
            combination.append(action)
        return combination
    
    def update(self, combination, reward):
        for i, gate in enumerate(combination):
            self.counts[i][gate] += 1
            n = 1 / self.counts[i][gate]
            q = self.q_values[i][gate]
            self.q_values[i][gate] = q + n * (reward - q)

    def best_combination(self):
        return [max(q, key=q.get) for q in self.q_values]