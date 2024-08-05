import heapq

def dijkstra(graph, start):
    # Ініціалізація: нескінченні відстані до всіх вершин, крім стартової
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо відстань до поточної вершини більша, ніж вже знайдена, пропустити
        if current_distance > distances[current_vertex]:
            continue

        # Оновлення відстаней до сусідів поточної вершини
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Якщо знайдена нова коротша відстань, оновити її
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад графа
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Виконати алгоритм Дейкстри від вершини 'A'
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

print("Найкоротші шляхи від вершини", start_vertex)
for vertex, distance in shortest_paths.items():
    print(f"Відстань до {vertex}: {distance}")
