import numpy as np


# ==============================
# 1. Demander le nombre d'états
# ==============================

n = int(input("Entrez le nombre d'états : "))

# ==============================
# 2. Saisir la matrice P
# ==============================

P = []

print("\nEntrez les valeurs de la matrice P :")

for i in range(n):
    ligne = []

    for j in range(n):
        valeur = float(input(f"P[{i+1}][{j+1}] = "))
        ligne.append(valeur)

    P.append(ligne)

P = np.array(P)

print("\nMatrice P :")
print(P)


# ==========================================
# 3. Vérifier que P est une matrice de transition
# ==========================================

def verifier_matrice_transition(P):
    n = len(P)

    # Vérifier que les valeurs sont entre 0 et 1
    if np.any(P < 0) or np.any(P > 1):
        return False, "Les valeurs doivent être comprises entre 0 et 1."

    # Vérifier que chaque ligne a une somme égale à 1
    for i in range(n):
        if not np.isclose(np.sum(P[i]), 1):
            return False, f"La ligne {i+1} ne possède pas une somme égale à 1."

    return True, "P est une matrice de transition."

valide, message = verifier_matrice_transition(P)

print("\nVérification :")
print(message)

# Si P n'est pas une matrice de transition, on arrête
if not valide:
    exit()

# ==========================================
# 4. Résoudre Pi P = Pi
# ==========================================

# Pour utiliser numpy.linalg.solve(), on transpose :
#
# (P.T - I) Pi.T = 0
#
# On remplace une équation par : somme(Pi) = 1

I = np.eye(n)

A = P.T - I
b = np.zeros(n)

# Remplacer la dernière équation par la condition :
# pi1 + pi2 + ... + pin = 1

A[-1] = np.ones(n)
b[-1] = 1


# ==========================================
# 5. Résolution du système
# ==========================================

Pi = np.linalg.solve(A, b)

# ==========================================
# 6. Afficher la distribution stationnaire
# ==========================================

print("\nDistribution stationnaire :")

for i in range(n):
    print(f"π{i+1} = {Pi[i]:.4f}")


print("\nVérification de la somme de πi:")
print(f"Somme = {np.sum(Pi):.2f}")


print("\nπ :")
print(Pi)