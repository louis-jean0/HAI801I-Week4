import random

def generate_initial_population(size):
    """ Générer une population initiale de stratégies aléatoires. """
    return [{'bet': random.uniform(0, 1), 'fold': random.uniform(0, 1)} for _ in range(size)]

def evaluate_strategy(strategy):
    """ Évaluer une stratégie en jouant plusieurs mains de poker. """
    # Simplification : performance aléatoire pour l'exemple
    return random.uniform(0, 100)

def select_parents(population, scores):
    """ Sélectionner les parents pour reproduction basée sur leur score. """
    total_score = sum(scores)
    selection_probs = [score / total_score for score in scores]
    return random.choices(population, weights=selection_probs, k=2)

def crossover(parent1, parent2):
    """ Recombiner deux parents pour créer un nouvel individu. """
    child = {'bet': (parent1['bet'] + parent2['bet']) / 2, 'fold': (parent1['fold'] + parent2['fold']) / 2}
    return child

def mutate(individual, mutation_rate=0.01):
    """ Introduire une mutation dans une stratégie. """
    if random.random() < mutation_rate:
        individual['bet'] += random.uniform(-0.1, 0.1)
        individual['fold'] += random.uniform(-0.1, 0.1)

def genetic_algorithm():
    population_size = 10
    num_generations = 50
    population = generate_initial_population(population_size)

    for _ in range(num_generations):
        scores = [evaluate_strategy(individual) for individual in population]
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = select_parents(population, scores)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        population = new_population

    best_strategy = max(population, key=evaluate_strategy)
    print("Meilleure stratégie trouvée:", best_strategy)

genetic_algorithm()
