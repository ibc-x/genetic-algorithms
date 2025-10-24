import random
# Paramètres
target = "Bonjour"
population_size = 100
mutation_rate = 0.01
generations = 1000
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
# Générer un individu aléatoire
def random_individual():
    return ''.join(random.choice(characters) for _ in range(len(target)))
# Calculer la fitness (plus c'est proche du mot cible, mieux c'est)
def fitness(individual):
    return sum(1 for i, c in enumerate(individual) if c == target[i])
# Sélection par tournoi
def selection(population):
    return max(random.choices(population, k=5), key=fitness)
# Croisement entre deux parents
def crossover(parent1, parent2):
    index = random.randint(0, len(target) - 1)
    return parent1[:index] + parent2[index:]
# Mutation aléatoire
def mutate(individual):
    return ''.join(
        c if random.random() > mutation_rate else random.choice(characters)
        for c in individual
    )
# Initialisation
population = [random_individual() for _ in range(population_size)]
# Évolution
for generation in range(generations):
    population = sorted(population, key=fitness, reverse=True)
    if fitness(population[0]) == len(target):
        print(f"Solution trouvée en {generation} générations : {population[0]}")
        break
    next_generation = [population[0]]  # Élites
    while len(next_generation) < population_size:
        parent1 = selection(population)
        parent2 = selection(population)
        child = crossover(parent1, parent2)
        child = mutate(child)
        next_generation.append(child)
    population = next_generation
else:
    print(f"Aucune solution trouvée après {generations} générations.")
    print(f"Meilleur individu : {population[0]} (fitness: {fitness(population[0])})")
