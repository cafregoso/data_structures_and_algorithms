def dfs(grafo, inicio):
    visitados = set()
    _dfs_recursivo(grafo, inicio, visitados)


def _dfs_recursivo(grafo, nodo, visitados):
    visitados.add(nodo)
    print(nodo, end=" ")

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            _dfs_recursivo(grafo, vecino, visitados)


# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Recorrido DFS:")
dfs(grafo, 'A')
