import numpy as np
from config import TRUTH_TABLE
from base.environment import Environment
from algorithms.epsilon_greedy import EpsilonGreedy
from algorithms.thompson_sampling import ThompsonSampling
from algorithms.ucb import UCB

def run_experiment(agent, env, name, n_iterations, table_name):
    print(f"\n--- {name} ---")
    
    for _ in range(n_iterations):
        combination = agent.choose_action()
        row = table_name[np.random.randint(0, len(table_name))]
        prediction = env.evaluate_combination(combination, row)

        if name == "Epsilon-Greedy":
            reward = 1 if prediction == row[-1] else -1
        else:
            reward = 1 if prediction == row[-1] else 0

        agent.update(combination, reward)
    
    best_comb = agent.best_combination()
    accuracy = env.calculate_accuracy(best_comb)
    
    print(f"Mejor combinación encontrada: {' -> '.join(best_comb)}")
    print(f"Precisión final: {accuracy}%")

    return accuracy

# Main program
def main():
    iterations = 1000
    epsilon = 0.1
    ucb_c = 2.0
    seed = 48
    
    np.random.seed(seed)

    truth_name = "NAND_XOR_PERFECT"
    current_table = TRUTH_TABLE[truth_name]

    env = Environment(current_table)
    gate_names = env.gates.names
    n_slots = env.n_slots

    print("========================================")
    print("             Prueba Bandits             ")
    print("========================================")
   
    while True:
        print("\n1. Configurar Parámetros")
        print("2. Configurar Tabla de Verdad")
        print("3. Ejecución Completa")
        print("4. Ejecutar Algoritmo Elegido")
        print("5. Salir del Programa")
        
        opcion = input("\nSelecciona una opción (1-5): ")
        
        if opcion == "5":
            print("\n========================================")
            print("         Simulación Finalizada          ")
            print("========================================")         
            break
        elif opcion == "1":
            try:
                iterations = int(input("Introduce el número de iteraciones [defecto 1000]: ") or 1000)
                epsilon = float(input("Epsilon para E-Greedy (0.0 a 1.0) [defecto 0.1]: ") or 0.1)
                ucb_c = float(input("Valor de exploración C para UCB [defecto 2.0]: ") or 2.0)
                print(f"Parámetros configurados: Iteraciones={iterations}, Epsilon={epsilon}, UCB_C={ucb_c}")
            except ValueError:
                print("Error: Debes introducir valores numéricos. Usando valores por defecto.")
                iterations, epsilon, ucb_c = 1000, 0.1, 2.0

        elif opcion == "2":
            print("\nTablas de Verdad Disponibles:")
            keys = list(TRUTH_TABLE.keys())
            for idx, key in enumerate(keys):
                print(f"{idx + 1}. {key}")
            
            try:
                sel = int(input("Selecciona el número de tabla: ")) - 1
                if 0 <= sel < len(keys):
                    truth_name = keys[sel]
                    current_table = TRUTH_TABLE[truth_name]
                    
                    env = Environment(current_table)
                    gate_names = env.gates.names
                    n_slots = env.n_slots
                    print(f"Tabla '{truth_name}' cargada")
                else:
                    print("Opción fuera de rango.")
            except ValueError:
                print("Por favor, introduce un número.")
        
        elif opcion == "3":
            print(f"\n[Config: {iterations}, tabla: {truth_name}]")
            run_experiment(EpsilonGreedy(n_slots, gate_names, epsilon=epsilon), env, "Epsilon-Greedy", iterations, current_table)
            run_experiment(ThompsonSampling(n_slots, gate_names), env, "Thompson Sampling", iterations, current_table)
            run_experiment(UCB(n_slots, gate_names, c=ucb_c), env, "UCB (Upper Confidence Bound)", iterations, current_table)

        elif opcion == "4":
            print("\n¿Cuál quieres probar?")
            print("a) Epsilon-Greedy\nb) Thompson Sampling\nc) UCB")
            algo = input("Elección: ").lower()
            print(f"\n[Config: {iterations}, tabla: {truth_name}]")
            
            if algo == 'a':
                run_experiment(EpsilonGreedy(n_slots, gate_names, epsilon=epsilon), env, "Epsilon-Greedy", iterations, current_table)
            elif algo == 'b':
                run_experiment(ThompsonSampling(n_slots, gate_names), env, "Thompson Sampling", iterations, current_table)
            elif algo == 'c':
                run_experiment(UCB(n_slots, gate_names, c=ucb_c), env, "UCB (Upper Confidence Bound)", iterations, current_table)

if __name__ == "__main__":
    main() 