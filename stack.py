
class Stack:

    def __init__(self) -> None:
        self.__elements = []


    def get_quantity(self) -> int:
        return len(self.__elements)


    def stack_item(self, value: int) -> None:
        try:
            if isinstance(value, int):
                self.__elements.append(value)
        except:
            raise ValueError("Elements must be int")


    def unstack_item(self) -> int | str:
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return "Stack is empty"


    def get_last_item(self) -> int | str:
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return "Stack is empty"


    last = property(fget=get_last_item)
    quantity = property(fget=get_quantity)

