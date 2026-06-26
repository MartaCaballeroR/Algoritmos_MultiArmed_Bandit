from .gates import Gates

class Environment:
    def __init__(self, truth_table):
        self.truth_table= truth_table
        self.gates = Gates()
        self.n_slots = len(truth_table[0]) - 2

    def evaluate_combination(self, combination, row):
        current_out = self.gates.evaluate(combination[0], row[0], row[1])
        for i in range(1, len(combination)):
            current_out = self.gates.evaluate(combination[i], current_out, row[i+1])
        return current_out
    
    def calculate_accuracy(self, combination):
        correct = 0
        for row in self.truth_table:
            if self.evaluate_combination(combination, row) == row[-1]:
                correct += 1
        return correct / len(self.truth_table) * 100