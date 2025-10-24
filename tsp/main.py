import random
import matplotlib.pyplot as plt
import math

# Liste des régions du Mali avec leurs coordonnées fictives (latitude, longitude)
regions = {
    "Kayes": (14.45, -11.44),
    "Koulikoro": (12.85, -7.55),
    "Sikasso": (11.32, -5.67),
    "Ségou": (13.43, -6.26),
    "Mopti": (14.49, -4.18),
    "Tombouctou": (16.77, -3.00),
    "Gao": (16.27, 0.05),
    "Kidal": (18.44, 1.41),
    "Bamako": (12.65, -8.00),
    "Taoudénit": (22.68, 0.50),
    "Ménaka": (15.91, 2.40),
    "Douentza": (15.00, -2.00),
    "Bandiagara": (14.35, -3.61),
    "Djenné": (13.90, -4.55),
    "San": (13.30, -4.90),
    "Yorosso": (11.75, -5.00),
    "Kolondieba": (11.25, -6.90),
    "Nioro": (14.25, -12.75),
    "Nara": (15.17, -6.00),
    "Goundam": (16.42, -3.67)
}


# Fonction pour calculer la distance euclidienne entre deux régions
def distance(region1, region2):
    x1, y1 = regions[region1]
    x2, y2 = regions[region2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Calcul de la distance totale d'un parcours
def total_distance(path):
    return sum(distance(path[i], path[i+1]) for i in range(len(path)-1)) + distance(path[-1], path[0])

# Générer un individu (parcours aléatoire)
def random_path():
    path = list(regions.keys())
    random.shuffle(path)
    return path

# Croisement entre deux parcours
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = parent1[start:end]
    for city in parent2:
        if city not in child:
            child.append(city)
    return child

# Mutation : échange de deux villes
def mutate(path, mutation_rate=0.05):
    path = path[:]
    for i in range(len(path)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(path)-1)
            path[i], path[j] = path[j], path[i]
    return path

# Sélection : tournoi
def selection(population):
    return min(random.sample(population, 5), key=total_distance)

# Paramètres
population_size = 100
generations = 200
mutation_rate = 0.05

# Initialisation
population = [random_path() for _ in range(population_size)]
best_distances = []

# Évolution
for gen in range(generations):
    population = sorted(population, key=total_distance)
    best_distances.append(total_distance(population[0]))
    next_generation = [population[0]]  # élitisme
    while len(next_generation) < population_size:
        parent1 = selection(population)
        parent2 = selection(population)
        child = crossover(parent1, parent2)
        child = mutate(child, mutation_rate)
        next_generation.append(child)
    population = next_generation

# Résultat final
best_path = population[0]
best_distance = total_distance(best_path)

# Affichage du parcours optimal
print("🗺️ Parcours optimal trouvé :")
print(" → ".join(best_path))
print(f"Distance totale estimée : {best_distance:.2f} unités")

# Visualisation de l'évolution de la distance
plt.plot(best_distances)
plt.title("Évolution de la distance minimale")
plt.xlabel("Générations")
plt.ylabel("Distance minimale")
plt.grid(True)
plt.tight_layout()
plt.savefig("evolution_distance_tsp_mali.png")
plt.show()
