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


def printAllPath(graph, start, end, visited, path):
    """ Find paths between start -> end using depth first search """
    visited[start] = True
    path.append(start)
    if start == end:
        print(path)
    else:
        for node in graph:
            if visited[node] is False:
                printAllPath(graph, node, end, visited, path)
    visited[start] = False
    path.pop()


v = dict()
for k, value in g.items():
    v[k] = False

printAllPath(g, 'a', 'b', v, [])
