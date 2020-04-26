import unittest
from .BigNumMult import BigNumMult


class MyTestCase(unittest.TestCase):
    def test_addNum(self):
        b = BigNumMult()
        self.assertEqual(b.numMult(973, 84), 81732)


if __name__ == '__main__':
    unittest.main()
