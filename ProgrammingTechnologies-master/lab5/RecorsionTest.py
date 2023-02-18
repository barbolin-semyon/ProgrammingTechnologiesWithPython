import unittest
from WorkWithRecursion import *

class MyTestCase(unittest.TestCase):
    def test_recursion_max(self):
        self.assertEqual(recursion_max([1, 67, 23, 399]), 399)
        self.assertEqual(recursion_max([1, 607, 23, 399]), 607)
        self.assertEqual(recursion_max([10000, 607, 23, 399]), 10000)

    def test_factorial(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_remove_v(self):
        self.assertEqual(remove_v("hellov"), "hello")
        self.assertEqual(remove_v("vvvv"), "")
        self.assertEqual(remove_v("hello"), "hello")

    def test_recursion_gcd(self):
        self.assertEqual(recursion_gcd(16, 12), 4)
        self.assertEqual(recursion_gcd(36, 12), 12)
        self.assertEqual(recursion_gcd(17, 12), 1)

if __name__ == '__main__':
    unittest.main()
