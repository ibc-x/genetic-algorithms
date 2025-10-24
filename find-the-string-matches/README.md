une version brute force de notre algorithme, sans utiliser d'algorithme génétique (AG). Le principe est simple : on génère toutes les combinaisons possibles de chaînes de la même longueur que le mot cible, et on vérifie si l'une d'elles correspond exactement au mot "Bonjour".
Cependant, comme le nombre de combinaisons est énorme (avec 53 caractères possibles et une longueur de 7, ça fait $53^7 \approx 1.5 \times 10^{12}$ combinaisons), ce code est théorique et ne doit pas être exécuté tel quel pour des raisons de performance

Complexité algorithmique
Le programme brute force explore toutes les combinaisons possibles de chaînes de caractères de longueur égale à celle du mot cible.
Paramètres :

Longueur du mot cible : $n = \text{len(target)} = 7$
Taille de l'alphabet : $a = \text{len(characters)} = 53$ (26 minuscules + 26 majuscules + espace)

Nombre total de combinaisons :
$a^n = 53^7 \approx 1.5 \times 10^{12}$
Complexité :

Temps : $O(a^n)$ → exponentielle
Espace : $O(1)$ (si on ne stocke pas les combinaisons, juste les génère et teste)

Temps d'exécution estimé
Supposons que notre ordinateur peut tester 1 million de combinaisons par seconde (ce qui est déjà optimiste).
Temps total :
$\frac{1.5 \times 10^{12}}{10^6} = 1.5 \times 10^6 \text{ secondes} \approx 17 \text{ jours}$
Et ça, juste pour un mot de 7 lettres ! Si tu augmentes la longueur ou la taille de l'alphabet, le temps explose.
