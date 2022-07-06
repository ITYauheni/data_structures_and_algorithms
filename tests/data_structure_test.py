from unittest import TestCase, main

from data_structures.stack import Stack
from data_structures.queue import Queue

class StackTest(TestCase):
    def setUp(self) -> None:
        self.stack = Stack()
        self.len_ = 0

    def test_stack(self):
        test_list = [1, 2, 3, 4, 5]

        for i in test_list:
            self.stack.push(i)
            self.len_ += 1
            self.assertEqual(len(self.stack), self.len_)

        for s, t in zip(self.stack, test_list[::-1]):
            self.assertEqual(s, t)

        self.assertEqual(self.stack.pop(), None)


class QueueTest(TestCase):
    def setUp(self) -> None:
        self.queue = Queue()
        self.len_ = 0

    def test_stack(self):
        test_list = [1, 2, 3, 4, 5]

        for i in test_list:
            self.queue.push(i)
            self.len_ += 1
            self.assertEqual(len(self.queue), self.len_)

        for s, t in zip(self.queue, test_list):
            self.assertEqual(s, t)

        self.assertEqual(self.queue.pop(), None)


if __name__ == "__main__":
    main()