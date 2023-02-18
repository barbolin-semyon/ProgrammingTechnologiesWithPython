import unittest
from WorkWithClosures import *

class MyTestCase(unittest.TestCase):
    def test_closure_sum(self):
        self.assertEqual(closure_sum(4)(4), 8)
        self.assertEqual(closure_sum(4)(0), 4)
        self.assertEqual(closure_sum(4)(16), 20)

    def test_closure_comparison(self):
        self.assertEqual(closure_comparison(">")("="), False)
        self.assertEqual(closure_comparison(">")(">"), True)
        self.assertEqual(closure_comparison("<")(">"), False)

    def test_closure_list_del(self):
        self.assertEqual(closure_list_del([1, 3, 12, 16, 21, 27, 30, 31])(3), [1, 16, 31])
        self.assertEqual(closure_list_del([])(3), [])
        self.assertEqual(closure_list_del([3])(3), [])

if __name__ == '__main__':
    unittest.main()
