# A simple Implementation of Graph

g = {
    'a': {'b', 'c', 'f'},
    'b': {'e', 'g'},
    'c': set(),
    'd': {'a', 'g'},
    'e': {'b', 'f'},
    'f': {'g'},
    'g': {'a', 'd', 'f'}
}


def dfs(graph, start):
    stack, visited = [start], set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            stack.extend(list(graph[node]-visited))


def bfs(graph, start):
    queue, visited = [start], set()
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node)
            queue.extend(list(graph[node]-visited))


bfs(g, 'a')
