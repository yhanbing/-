import unittest
from .MyHashMap import MyHashMap


class MyTestCase(unittest.TestCase):
    def test_put(self):
        m = MyHashMap(3)
        m.put(2, 4)
        self.assertEqual(m.hash, [[], [], [[2, 4]]])

    def test_get(self):
        m = MyHashMap(3)
        m.put(2, 4)
        self.assertEqual(m.get(2), 4)

    def test_remove(self):
        m = MyHashMap(3)
        m.put(1, 4)
        m.put(2, 3)
        m.remove(1)
        self.assertEqual(m.hash, [[], [], [[2, 3]]])


if __name__ == '__main__':
    unittest.main()
