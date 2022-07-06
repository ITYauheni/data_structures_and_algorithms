from unittest import TestCase, main
from random import randint

from alghoritms.sort_algs import selection_sort, insertion_sort, bubble_sort

sort_methods = [insertion_sort, selection_sort, bubble_sort]


class SortAlgTest(TestCase):

    def test_sort(self):
        test_list = list(randint(-100, 100) for i in range(randint(10, 15)))

        for func in sort_methods:
            self.assertEqual(func(test_list), sorted(test_list))
            self.assertEqual(func(test_list, reverse=True), sorted(test_list, reverse=True))

    def test_not_iterable(self):
        with self.assertRaises(TypeError):
            sort_methods(1)



if __name__ == "__main__":
    main()
