import unittest

from WorkWithDecorate import *


class MyTestCase(unittest.TestCase):
    def test_str_case_result(self):
        f = str_case_result(del_str)
        self.assertEqual(f("hello", 'l'), "Heo")
        self.assertEqual(f("МеЖнацИоНаЛьНыЙ", 'а'), "МЕЖНЦИонльный")
        self.assertEqual(f("hello", 'l'), "Heo")

    def test_celsius(self):
        f = celsius(temperature_fahrenheit)
        self.assertEqual(f(33.8), 1)
        self.assertEqual(f(67.6), 2)

    def test_check_type(self):
        f = check_type(reply_int)
        self.assertEqual(f(5), 10)
        self.assertEqual(f(0), 0)
        self.assertEqual(f("dsf"), None)


if __name__ == '__main__':
    unittest.main()
