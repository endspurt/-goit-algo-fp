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
    plt.savefig("monte_carlo_probabilities.png")
    plt.show()

num_rolls = 100000
probabilities = monte_carlo_simulation(num_rolls)
plot_probabilities(probabilities)

# Аналітичні ймовірності для порівняння
analytical_probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
comparison_results = []

for sum_value, probability in zip(range(2, 13), analytical_probabilities):
    monte_carlo_probability = probabilities[sum_value]
    comparison_results.append((sum_value, probability, monte_carlo_probability))
    print(f"Сума: {sum_value}, Аналітична імовірність: {probability:.4f}, Імітаційна імовірність: {monte_carlo_probability:.4f}")

# Запис результатів у файл readme.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write("# Порівняння імовірностей сум при киданні двох кубиків\n\n")
    f.write("Цей файл містить порівняння між аналітичними імовірностями та імітаційними імовірностями, отриманими за допомогою методу Монте-Карло. Результати імітації засновані на 100000 кидках двох кубиків.\n\n")
    f.write("| Сума | Аналітична імовірність | Імітаційна імовірність |\n")
    f.write("|------|------------------------|-----------------------|\n")
    for sum_value, analytical, monte_carlo in comparison_results:
        f.write(f"| {sum_value} | {analytical:.4f} | {monte_carlo:.4f} |\n")

    f.write("\n## Висновки\n")
    f.write("На основі результатів порівняння можна зробити висновок, що імітаційні імовірності, отримані за допомогою методу Монте-Карло, дуже близькі до аналітичних імовірностей. Це демонструє правильність розрахунків та ефективність методу Монте-Карло для подібних задач.\n")
    f.write("Невеликі відхилення між імітаційними та аналітичними імовірностями можуть бути пояснені випадковим характером імітаційного процесу. Проте, загальна тенденція та відповідність результатів підтверджують, що метод Монте-Карло є надійним підходом для оцінки ймовірностей.\n")
