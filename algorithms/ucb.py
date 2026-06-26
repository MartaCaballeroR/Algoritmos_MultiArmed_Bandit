import numpy as np
import random
from base.initial import Initial

class UCB:
    def __init__(self, n_slots, gate_names, c=2.0):
        self.n_slots = n_slots                  
        self.gate_names = gate_names            
        self.c = c                              
        self.total_steps = 0
        self.q_values = Initial.initial_q_values(n_slots, gate_names)
        self.counts = Initial.initial_counts(n_slots, gate_names)

    def choose_action(self):
        combination = []
        self.total_steps += 1
        for i in range(self.n_slots):
            ucb_values = {}
            for gate in self.gate_names:
                if self.counts[i][gate] == 0:
                    ucb_values[gate] = float('inf')
                else:
                    reward = self.q_values[i][gate]
                    exploration = self.c * np.sqrt(
                        np.log(self.total_steps) / self.counts[i][gate]
                    )
                    ucb_values[gate] = reward + exploration
            max_value = max(ucb_values.values())
            best_candidates = [g for g, v in ucb_values.items() if v == max_value]
            best_gate = random.choice(best_candidates)
            combination.append(best_gate)
        return combination

    def update(self, combination, reward):
        for i, gate in enumerate(combination):
            self.counts[i][gate] += 1
            n = self.counts[i][gate]
            q = self.q_values[i][gate]
            self.q_values[i][gate] = q + (reward - q) / n

    def best_combination(self):
        best = []
        for i in range(self.n_slots):
            max_value = max(self.q_values[i].values())
            best_candidates = [g for g, v in self.q_values[i].items() if v == max_value]
            best.append(random.choice(best_candidates))
        return best