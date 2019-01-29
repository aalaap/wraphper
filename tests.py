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

    def test_str_replace(self):
        # str, str, str
        self.assertEqual(php.str_replace('world', 'universe', 'Hello, world!'), 'Hello, universe!')

        # str, str, str, count
        self.assertEqual(php.str_replace('the', 'a', 'the quick brown fox jumps over the lazy dog', 1), 'a quick brown fox jumps over the lazy dog')

        # list, str, str
        self.assertEqual(php.str_replace(['the', 'The'], 'a', 'The quick brown fox jumps over the lazy dog'), 'a quick brown fox jumps over a lazy dog')

        # str, list, str
        # nonsensical implementation

        # list, list, str
        self.assertEqual(php.str_replace(['quick', 'brown', 'lazy'], ['slow', 'grey', 'quick'], 'The quick brown fox jumps over the lazy dog'), 'The slow grey fox jumps over the quick dog')

        # str, str, list
        self.assertEqual(php.str_replace('the', 'only', ['the good', 'the bad', 'the ugly']), ['only good', 'only bad', 'only ugly'])

if __name__ == '__main__':
    unittest.main()