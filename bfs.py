from collections import deque


def bfs(grafo, inicio):
    visitados = set()
    cola = deque()
    cola.append(inicio)
    visitados.add(inicio)

    while cola:
        nodo_actual = cola.popleft()
        print(nodo_actual, end=" ")

        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:
                cola.append(vecino)
                visitados.add(vecino)


# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Recorrido BFS:")
bfs(grafo, 'D')
