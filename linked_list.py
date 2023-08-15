
class LinkedList:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None) -> None:
            self._element = element
            self._next = next

    _first = None
    _last = None
    _quantity = 0

    def __init__(self, value: int | str) -> None:
        self._first = self._Node(value)
        self._last = self._first
        self._quantity += 1

    def _get_quantity(self) -> int:
        return self._quantity

    def _get_first(self) -> int | str:
        return self._first
    
    def _get_last(self) -> int | str:
        if self._quantity == 1:
            return self._first
        else:
            return self._last
    
    def insert(self, value: int | str) -> None:
        new_node = self._Node(value)
        self._last.next = new_node
        self._last = new_node
        self._quantity += 1

    def insert_at_position(self, value: int | str, position: int): 
        if position < 0 or position > self._quantity:
            raise ValueError("Position out of range")
        
        actual = self._first
        new_node = self._Node(value)

        if position == 0:
            new_node.next = self._first
            self._first = new_node
            self._quantity += 1
        else:
            for i in range(position - 1):
                actual = actual.next
            aux = actual.next
            actual.next = new_node
            new_node.next = actual.next
            if position == self._quantity:
                self._last = new_node
        
        self._quantity += 1

    def position(self, value: int) -> int:
        actual = self._first
        position = 0
        while actual.value != value:
            actual = actual.next
            position += 1
        return position

    def delete(self, value: int | str) -> None:
        position = self.position(value)
        if position == -1:
            raise ValueError("Value not found")
        
        if position == 0:
            self._first = self._first.next
            self._quantity -= 1
        else:
            actual = self._first
            for _ in range(position - 1):
                actual = actual.next
            actual.next = actual.next.next

            if position == self._quantity - 1:
                self._last = actual
            self._quantity -= 1

    def get_elements(self) -> list:
        elements = []
        actual = self._first
        while actual != None:
            elements.append(actual.value)
            actual = actual.next
        return elements
    