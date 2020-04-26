import unittest
from .BigNumAdd import BigNumAdd


class MyTestCase(unittest.TestCase):

    def test_addNum(self):
        b = BigNumAdd()
        self.assertEqual(b.addNum(99, 8), "107")

    def test_invalid(self):
        b = BigNumAdd()
        with self.assertRaises(TypeError):
            b.addNum()


if __name__ == '__main__':
    unittest.main()
