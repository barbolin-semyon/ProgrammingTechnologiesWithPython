import unittest
from WorkWithFunc import add, max_number, find_list_index, algebraic_sum, month_days

class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add([1, 6, 4], [3]), 14)
        self.assertEqual(add([1, 6, 4], [3, 2]), 16)
        self.assertEqual(add([1, 6, 4], [3, -5]), 9)

    def test_max_number(self):
        self.assertEqual(max_number([1, 6, 4]), 6)
        self.assertEqual(max_number([100, 6, 4]), 100)
        self.assertEqual(max_number([100, 60000, 4]), 60000)

    def test_find_list_index(self):
        self.assertEqual(find_list_index([1, 3, 5], 5), 2)
        self.assertEqual(find_list_index([1, 3, 5], 3), 1)
        self.assertEqual(find_list_index([1, 3, 5], 1), 0)

    def test_month_days(self):
        self.assertEqual(month_days(0), 0)
        self.assertEqual(month_days(2), 28)
        self.assertEqual(month_days(1), 31)

    def test_algebraic_sum(self):
        self.assertEqual(algebraic_sum(1), 1)
        self.assertEqual(algebraic_sum(2), 5)
        self.assertEqual(algebraic_sum(2, 3), 9)

if __name__ == '__main__':
    unittest.main()
