import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def monte_carlo_simulation(num_rolls):
    sums = [0] * 13  # Індекси від 0 до 12, але використовуємо тільки від 2 до 12
    for _ in range(num_rolls):
        result = roll_dice()
        sums[result] += 1

    probabilities = [s / num_rolls for s in sums]
    return probabilities

def plot_probabilities(probabilities):
    sums = list(range(2, 13))
    plt.bar(sums, probabilities[2:], tick_label=sums)
    plt.xlabel('Сума')
    plt.ylabel('Імовірність')
    plt.title('Імовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.show()

num_rolls = 100000
probabilities = monte_carlo_simulation(num_rolls)
plot_probabilities(probabilities)

# Аналітичні ймовірності для порівняння
analytical_probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
for sum_value, probability in zip(range(2, 13), analytical_probabilities):
    print(f"Сума: {sum_value}, Аналітична імовірність: {probability:.4f}, Імітаційна імовірність: {probabilities[sum_value]:.4f}")
