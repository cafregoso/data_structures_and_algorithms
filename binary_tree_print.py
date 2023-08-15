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

    def imprimir_preorden(self):
        self._imprimir_preorden_recursivo(self.raiz)

    def _imprimir_preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=" ")
            self._imprimir_preorden_recursivo(nodo.izquierda)
            self._imprimir_preorden_recursivo(nodo.derecha)

    def imprimir_enorden(self):
        self._imprimir_enorden_recursivo(self.raiz)

    def _imprimir_enorden_recursivo(self, nodo):
        if nodo is not None:
            self._imprimir_enorden_recursivo(nodo.izquierda)
            print(nodo.valor, end=" ")
            self._imprimir_enorden_recursivo(nodo.derecha)

    def imprimir_postorden(self):
        self._imprimir_postorden_recursivo(self.raiz)

    def _imprimir_postorden_recursivo(self, nodo):
        if nodo is not None:
            self._imprimir_postorden_recursivo(nodo.izquierda)
            self._imprimir_postorden_recursivo(nodo.derecha)
            print(nodo.valor, end=" ")


# Ejemplo de uso
arbol = ArbolBinarioBusqueda()
arbol.insertar(8)
arbol.insertar(3)
arbol.insertar(10)
arbol.insertar(1)
arbol.insertar(6)
arbol.insertar(14)

print("Preorden:")
arbol.imprimir_preorden()
print("\nEnorden:")
arbol.imprimir_enorden()
print("\nPostorden:")
arbol.imprimir_postorden()
