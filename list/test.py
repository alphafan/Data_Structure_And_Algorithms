import unittest
from .list import List


class TestList(unittest.TestCase):

    # ---------------------------------------------
    # Test add an element
    # ---------------------------------------------

    def test_insert(self):
        lst = List()
        lst.insert('a')
        lst.insert('b')
        lst.insert('c')
        print(lst)

    # ---------------------------------------------
    # Test insert an element
    # ---------------------------------------------

    def test_insert_at_1(self):
        lst = List()
        lst.insertAt('a', 0)
        print(lst)

    def test_insert_at_2(self):
        lst = List()
        lst.insertAt('a', 0)
        lst.insertAt('b', 1)
        print(lst)

    def test_insert_at_3(self):
        lst = List()
        lst.insertAt('a', 0)
        lst.insertAt('c', 0)
        lst.insertAt('b', 1)
        print(lst)

    def test_insert_at_4(self):
        lst = List()
        lst.insertAt('a', 0)
        lst.insertAt('b', 1)
        lst.insertAt('c', 0)
        print(lst)

    def test_insert_at_5(self):
        lst = List()
        lst.insertAt('a', 0)
        lst.insertAt('b', 1)
        print(lst)

    # ---------------------------------------------
    # Test delete element
    # ---------------------------------------------

    def test_delete_1(self):
        lst = List()
        lst.insert('a')
        lst.delete('a')
        print(lst)

    def test_delete_2(self):
        lst = List()
        lst.insert('a')
        lst.insert('b')
        lst.delete('a')
        print(lst)

    def test_delete_3(self):
        lst = List()
        lst.insert('b')
        lst.insert('a')
        lst.delete('a')
        print(lst)

    def test_delete_4(self):
        lst = List()
        lst.insert('a')
        lst.insert('b')
        lst.insert('c')
        lst.delete('b')
        print(lst)

    def test_delete_5(self):
        lst = List()
        lst.insert('a')
        lst.delete('b')
        print(lst)

    def test_delete_6(self):
        lst = List()
        lst.insert('a')
        lst.insert('a')
        lst.delete('a')
        print(lst)

    def test_delete_7(self):
        lst = List()
        lst.insert('a')
        lst.insert('b')
        lst.insert('b')
        lst.insert('c')
        lst.delete('b')
        print(lst)

    # ---------------------------------------------
    # Test delete at position
    # ---------------------------------------------

    def test_delete_at_1(self):
        lst = List()
        lst.insert('a')
        lst.insert('b')
        lst.deleteAt(0)
        print(lst)

    def test_delete_at_2(self):
        lst = List()
        lst.insert('a')
        lst.insert('b')
        lst.deleteAt(1)
        print(lst)

    def test_delete_at_3(self):
        lst = List()
        lst.insert('a')
        lst.deleteAt(0)
        print(lst)

    # ---------------------------------------------
    # Test delete all elements with value
    # ---------------------------------------------

    def test_delete_all_1(self):
        lst = List()
        lst.insert('a')
        lst.insert('b')
        lst.insert('b')
        lst.insert('c')
        lst.deleteAll('b')
        print(lst)

    def test_delete_all_2(self):
        lst = List()
        lst.insert('a')
        lst.insert('b')
        lst.insert('b')
        lst.deleteAll('b')
        print(lst)

    def test_delete_all_3(self):
        lst = List()
        lst.insert('a')
        lst.insert('b')
        lst.insert('c')
        lst.insert('b')
        lst.deleteAll('b')
        print(lst)

    def test_delete_all_4(self):
        lst = List()
        lst.insert('b')
        lst.insert('b')
        lst.insert('c')
        lst.insert('b')
        lst.deleteAll('b')
        print(lst)

    def test_delete_all_5(self):
        lst = List()
        lst.insert('b')
        lst.deleteAll('b')
        print(lst)

    def test_delete_all_6(self):
        lst = List()
        lst.insert('b')
        lst.insert('b')
        lst.deleteAll('b')
        print(lst)

    def test_delete_all_7(self):
        lst = List()
        lst.insert('b')
        lst.insert('a')
        lst.deleteAll('b')
        print(lst)

    # ---------------------------------------------
    # Test reverse element(s)
    # ---------------------------------------------

    def test_reverse_1(self):
        lst = List()
        lst.insert('b')
        lst.insert('a')
        lst.reverse()
        print(lst)

    def test_reverse_2(self):
        lst = List()
        lst.insert('b')
        lst.reverse()
        print(lst)

    def test_reverse_3(self):
        lst = List()
        lst.insert('b')
        lst.insert('a')
        lst.insert('c')
        lst.reverse()
        print(lst)

    def test_reverse_4(self):
        lst = List()
        lst.reverse()
        print(lst)


if __name__ == '__main__':
    unittest.main()
