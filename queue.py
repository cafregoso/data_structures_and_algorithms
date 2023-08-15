
class Queue:

    def __init__(self) -> None:
        self.__elements = []


    def get_quantity(self) -> int:
        return len(self.__elements)


    def enqueue(self, value: int) -> None:
        try:
            if isinstance(value, int):
                self.__elements.append(value)
        except:
            raise ValueError("Elements must be an int")


    def dequeue(self) -> int | str:
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return "Queue is empty"


    def first_element(self) -> int | str:
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return "Queue is empty!"
