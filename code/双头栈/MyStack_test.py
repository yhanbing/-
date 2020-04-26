import unittest
from .MyStack import MyStack


class MyTestCase(unittest.TestCase):
    def test_l_push(self):
        m = MyStack()
        m.l_push(2)
        m.l_push(3)
        self.assertEqual(m.stack, [3, 2])

    def test_r_push(self):
        m = MyStack()
        m.r_push(2)
        m.r_push(3)
        self.assertEqual(m.stack, [2, 3])

    def test_l_pop(self):
        m = MyStack()
        m.r_push(2)
        m.r_push(3)
        m.l_pop()
        self.assertEqual(m.stack, [3])

    def test_r_pop(self):
        m = MyStack()
        m.r_push(2)
        m.r_push(3)
        m.r_pop()
        self.assertEqual(m.stack, [2])


if __name__ == '__main__':
    unittest.main()
