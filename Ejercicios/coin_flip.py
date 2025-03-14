import random


def simulate_coin_flips():
    # Genera 100 lanzamientos de moneda (H o T)
    flips = [random.choice(["H", "T"]) for _ in range(100)]
    return flips


def has_streak(flips):
    # Verifica si hay una racha de 6 consecutivos iguales
    streak_count = 1
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            streak_count += 1
            if streak_count == 6:
                return True
        else:
            streak_count = 1
    return False


# Parte principal del experimento
numberOfStreaks = 0
experiments = 10000

for _ in range(experiments):
    flips = simulate_coin_flips()
    if has_streak(flips):
        numberOfStreaks += 1

# Calcula el porcentaje de experimentos con rachas
percentage = (numberOfStreaks / experiments) * 100
print(f"Chance of streak: {percentage:.2f}%")
print(has_streak(flips))
