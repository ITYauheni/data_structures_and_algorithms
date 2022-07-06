class Queue:

    __tail = None
    __length = 0

    class __Node:

        def __init__(self, value):
            self.value = value
            self.next = None

    def push(self, value):
        if self.__tail is None:
            self.__tail = self.__Node(value)
            self.__length += 1
            return

        head = self.__tail
        while head:
            if head.next is None:
                break
            head = head.next
        head.next = self.__Node(value)
        self.__length += 1

    def pop(self):
        tmp = self.__tail
        if tmp is None:
            return tmp
        self.__tail = self.__tail.next
        self.__length -= 1
        return tmp.value

    def __iter__(self):
        while True:
            tmp = self.pop()
            if tmp is None:
                break
            yield tmp

    def __len__(self):
        return self.__length

    def __bool__(self):
        return bool(self.__tail)


if __name__ == "__main__":
    queue = Queue()
    print(bool(queue))
    print(queue.__len__())
    queue.push(1)
    print(bool(queue))
    print(queue.__len__())

