# genetic-algorithms
* L'objectif est de trouver une chaîne de caractères qui correspond exactement à un mot cible, par exemple "Bonjour".
* Notre algorithme génétique est composé de :
  * Individu: une chaîne de caractères de même longueur que le mot cible.
  * Population: un ensemble d’individus générés aléatoirement.
  * Fitness: fonction qui mesure à quel point un individu est proche du mot cible.
  * Sélection: On choisit les meilleurs individus pour se reproduire. Ici, on utilise une sélection par tournoi.
  * Croisement (crossover): On combine deux parents pour créer un enfant.
  * Mutation: On modifie aléatoirement un caractère de l’individu avec une petite probabilité.  
* Cycle d’évolution: à chaque génération:
  * On trie la population par fitness.
  * On garde le meilleur (élitisme).
  * On crée une nouvelle génération par croisement et mutation.
  * On répète jusqu’à trouver la solution ou atteindre le nombre max de générations.
