class Stack:
    """A stack is an ordered set of data
    in which the placement of new elements and the removal of existing ones is carried out only at one end of it,
    which is called the top of the stack.

    principle of "last in first out" (LIFO)

    push(item) - adds the item to the top of stack

    pop() - removes and returns item from the top of the stack"""

    __head = None
    __length = 0

    class Node:
        def __init__(self, value, previous=None):
            self.value = value
            self.previous = previous

    def push(self, value):
        """adds the item to the top of stack"""
        if self.__length == 0:
            self.__head = self.Node(value)
        else:
            previous = self.__head
            self.__head = self.Node(value, previous)

        self.__length += 1

    def pop(self):
        """removes and returns item from the top of the stack"""
        node = self.__head
        if node is None:
            return node
        self.__head = self.__head.previous
        self.__length -= 1
        return node.value

    def __iter__(self):
        while True:
            tmp = self.pop()
            if tmp is None:
                break
            yield tmp

    def __len__(self):
        return self.__length

    def __bool__(self):
        return bool(self.__length)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(len(stack))
    print(bool(stack))
    stack.pop()
    for i in stack:
        print(i)
    print(len(stack))
    print(bool(stack))


