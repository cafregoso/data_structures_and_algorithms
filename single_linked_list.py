
class LinkedList:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None) -> None:
            self._element = element
            self._next = next


    def __init__(self) -> None:
        """Create an empty list"""
        self._head = None
        self._size = 0


    def __len__(self):
        """Return a number of elements in the list"""
        return self._size


    def is_empty(self):
        """Return True if the list is empty"""
        return self._size == 0


    def push(self, node):
        """Add element at the top of the list"""
        self._head = self._Node(node, self._head)
        self._size += 1


    def get_top(self):
        """Return without remove the top element in the list
        or
            Raise Empty exception if the list is empty
        """
        if self.is_empty():
            raise Exception("List is empty")
        return self._head._element


    def remove_top(self):
        """Remove and return top element in the list
        or
            raise an Exception if its empty
        """
        if self.is_empty():
            raise Exception("List is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
