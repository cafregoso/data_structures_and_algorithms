from queue import Queue

class Arbol:
    _valor = None
    _hijos = None

    def __init__(self, valor, hijos = []) -> None:
        self._valor = valor
        self._hijos = []
        for hijo in hijos:
            self._hijos.append(Arbol(hijo))

    def agrega_hijo(self, hijo):
        self._hijos.append(hijo)
    
    def buscar(self, valor):
        return self.recorrido(buscar = valor)
    
    def eliminar(self, valor):
        return self.recorrido(eliminar = valor)
    
    def recorrido(self, imprimir = False, buscar = None, eliminar = None):
        # Para eliminar subarboles
        if eliminar and eliminar == self._valor:
            self._valor = None
            self._hijos = []
            return True
        
        q=Queue()
        q.enqueue(self)

        while q.get_quantity() > 0:
            # Para imprimir el arbol
            if imprimir:
                print(q.first_element()._valor)
            
            # Para buscar un valor
            if buscar and buscar == q.first_element()._valor:
                return q.first_element()
            actual = q.first_element()
            for i in range(len(actual._hijos)):
                # Para eliminar un subarbol
                if eliminar and eliminar == actual._hijos[i]._valor:
                    actual._hijos.pop(i)
                    return True
                q.enqueue(actual._hijos[i])
            q.dequeue()

    def dame_hijos(self):
        return self._hijos
    
    def dame_valor(self):
        return self._valor
    
    def define_valor(self, valor):
        self._valor = valor

    def __str__(self) -> str:
        return str(self._valor)
