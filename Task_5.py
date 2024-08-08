import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_nodes=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if visited_nodes is None:
        visited_nodes = {}

    colors = [visited_nodes.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs_traversal(root):
    stack = [root]
    visited_nodes = {}
    step = 0
    while stack:
        node = stack.pop()
        if node and node.id not in visited_nodes:
            color = plt.cm.viridis(step / 20)  # Генерація кольору на основі порядку відвідування
            visited_nodes[node.id] = color
            step += 1
            stack.append(node.right)
            stack.append(node.left)
    return visited_nodes

def bfs_traversal(root):
    queue = deque([root])
    visited_nodes = {}
    step = 0
    while queue:
        node = queue.popleft()
        if node and node.id not in visited_nodes:
            color = plt.cm.plasma(step / 20)  # Генерація кольору на основі порядку відвідування
            visited_nodes[node.id] = color
            step += 1
            queue.append(node.left)
            queue.append(node.right)
    return visited_nodes

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева з обходом в глибину
dfs_visited = dfs_traversal(root)
draw_tree(root, dfs_visited)

# Відображення дерева з обходом в ширину
bfs_visited = bfs_traversal(root)
draw_tree(root, bfs_visited)
