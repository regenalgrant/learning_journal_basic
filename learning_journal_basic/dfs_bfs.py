"""DFS and BFS."""
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'A'],
    'C': ['A'],
    'D': ['B']
}

class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_all(self, from_node, to_node):
        return self.weights[(from_node + to_node)]

def dfs(graph, start, goal):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)

            if node == goal:
                return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


def bfs(graph, start, goal):
    # maintain q paths
    queue = []
    # irst path into the queue
    queue.append([start])
    while queue:
        # irst path from the queue
        path = queue.pop(0)
        # last node from the path
        node = path[-1]
        # path found
        if node == goal:
            return path
        # adjacent nodes, construct path and push it to queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

if __name__ == '__main__':
