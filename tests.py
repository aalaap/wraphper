import unittest
from wraphper import wraphper as php

class PythonPHPTestCase(unittest.TestCase):
    """Test cases for the wraphper module"""

    def test_count(self):
        c = php.count([1, 2, 3])
        self.assertEqual(c, 3)

if __name__ == '__main__':
    unittest.main()