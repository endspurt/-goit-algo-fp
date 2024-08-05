items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортувати предмети за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []
    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            total_calories += info['calories']
            selected_items.append(item)
    return total_calories, selected_items

def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost, calories = info['cost'], info['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, info = item_list[i - 1]
            selected_items.append(name)
            w -= info['cost']
    
    return total_calories, selected_items

# Приклад використання
budget = 100

greedy_result = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм: {greedy_result}")

dp_result = dynamic_programming(items, budget)
print(f"Динамічне програмування: {dp_result}")
