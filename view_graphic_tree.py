from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo.derecha)

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar_recursivo(valor, nodo.izquierda)
        return self._buscar_recursivo(valor, nodo.derecha)

    def imprimir_arbol(self):
        self._imprimir_arbol_recursivo(self.raiz, "", True)

    def _imprimir_arbol_recursivo(self, nodo, prefijo, es_ultimo):
        if nodo is not None:
            print(prefijo, end="")
            print("└──" if es_ultimo else "├──", end="")
            print(nodo.valor)
            prefijo += "    " if es_ultimo else "│   "
            self._imprimir_arbol_recursivo(nodo.izquierda, prefijo, False)
            self._imprimir_arbol_recursivo(nodo.derecha, prefijo, True)

    def altura(self):
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        if nodo is None:
            return 0
        altura_izquierda = self._altura_recursiva(nodo.izquierda)
        altura_derecha = self._altura_recursiva(nodo.derecha)
        return max(altura_izquierda, altura_derecha) + 1

    def anchura(self):
        if self.raiz is None:
            return 0
        cola = deque()
        cola.append(self.raiz)
        nivel_actual = 1
        max_anchura = 1
        while len(cola) > 0:
            nivel_actual_anchura = len(cola)
            max_anchura = max(max_anchura, nivel_actual_anchura)
            for _ in range(nivel_actual_anchura):
                nodo = cola.popleft()
                if nodo.izquierda is not None:
                    cola.append(nodo.izquierda)
                if nodo.derecha is not None:
                    cola.append(nodo.derecha)
            nivel_actual += 1
        return max_anchura


# Ejemplo de uso
arbol = ArbolBinarioBusqueda()
arbol.insertar(8)
arbol.insertar(3)
arbol.insertar(10)
arbol.insertar(1)
arbol.insertar(6)
arbol.insertar(14)
arbol.insertar(9)
arbol.insertar(4)
arbol.insertar(2)
arbol.insertar(11)

altura = arbol.altura()
anchura = arbol.anchura()
arbol.imprimir_arbol()
print("Altura:", altura)
print("Anchura:", anchura)
