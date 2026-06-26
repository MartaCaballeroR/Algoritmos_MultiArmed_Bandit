class Initial:

    # Epsilon-Greedy UCB
    @staticmethod
    def initial_q_values(n_slots, gate_names):
        return [{gate: 0.0 for gate in gate_names} for _ in range(n_slots)]
    
    @staticmethod
    def initial_counts(n_slots, gate_names):
        return [{gate: 0 for gate in gate_names} for _ in range(n_slots)]
    
    # Thompson Sampling
    @staticmethod
    def initial_alpha(n_slots, gate_names):
        return [{gate: 1 for gate in gate_names} for _ in range(n_slots)]
    
    @staticmethod
    def initial_beta(n_slots, gate_names):
        return [{gate: 1 for gate in gate_names} for _ in range(n_slots)]