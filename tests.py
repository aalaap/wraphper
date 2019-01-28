import unittest
import wraphper as php

class PythonPHPTestCase(unittest.TestCase):
    """Test cases for the wraphper module"""

    def test_count(self):
        test_list = [1, 2, 3]
        test_dict = {1:'value','key':2}
        test_tuple = (1, 2, 3, 4)

        self.assertEqual(php.count(test_list), 3)
        self.assertEqual(php.count(test_dict), 2)
        self.assertEqual(php.count(test_tuple), 4)

if __name__ == '__main__':
    unittest.main()