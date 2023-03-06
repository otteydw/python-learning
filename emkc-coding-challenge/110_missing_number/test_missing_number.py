import unittest

from missing_number import find_missing_number

class MyTests(unittest.TestCase):
    def test_find_missing_number(self):
        self.assertEqual(find_missing_number('1,3,4'), 2)
        self.assertEqual(find_missing_number('3,2,1,2,4'), 3)
        self.assertEqual(find_missing_number('1,1,1,1,2,3,4,5,6,7,8,10,9,8'), 9)

if __name__ == "__main__":
    unittest.main()
