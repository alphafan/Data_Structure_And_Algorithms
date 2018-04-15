import unittest
from .interval_tree import IntervalTree, TreeNode, Interval


class TestInterval(unittest.TestCase):

    # -----------------------------------------
    # Test Insert Single Node
    # -----------------------------------------

    def test_insert_1(self):
        tree = IntervalTree()
        root = TreeNode(3, 4, 7)
        root = tree.insert(root, Interval(1, 2, 5))
        assert root.left.start == 1
        assert root.left.end == 2
        assert root.left.minPrice == 5

    def test_insert_2(self):
        tree = IntervalTree()
        root = TreeNode(3, 4, 7)
        root = tree.insert(root, Interval(1, 3, 5))
        assert root.left.start == 1
        assert root.left.end == 3
        assert root.left.minPrice == 5

    def test_insert_3(self):
        tree = IntervalTree()
        root = TreeNode(3, 4, 7)
        root = tree.insert(root, Interval(1, 4, 5))
        assert root.start == 3
        assert root.end == 4
        assert root.minPrice == 5
        assert root.left.start == 1
        assert root.left.end == 3
        assert root.left.minPrice == 5

    def test_insert_4(self):
        tree = IntervalTree()
        root = TreeNode(3, 5, 7)
        root = tree.insert(root, Interval(1, 4, 5))
        assert root.start == 4
        assert root.end == 5
        assert root.minPrice == 7
        assert root.left.start == 1
        assert root.left.end == 4
        assert root.left.minPrice == 5

    def test_insert_5(self):
        tree = IntervalTree()
        root = TreeNode(3, 5, 7)
        root = tree.insert(root, Interval(1, 5, 5))
        assert root.start == 3
        assert root.end == 5
        assert root.minPrice == 5
        assert root.left.start == 1
        assert root.left.end == 3
        assert root.left.minPrice == 5

    def test_insert_6(self):
        tree = IntervalTree()
        root = TreeNode(3, 5, 7)
        root = tree.insert(root, Interval(1, 6, 5))
        assert root.start == 3
        assert root.end == 5
        assert root.minPrice == 5
        assert root.left.start == 1
        assert root.left.end == 3
        assert root.left.minPrice == 5
        assert root.right.start == 5
        assert root.right.end == 6
        assert root.right.minPrice == 5

    def test_insert_7(self):
        tree = IntervalTree()
        root = TreeNode(3, 5, 7)
        root = tree.insert(root, Interval(1, 6, 10))
        assert root.start == 3
        assert root.end == 5
        assert root.minPrice == 7
        assert root.left.start == 1
        assert root.left.end == 3
        assert root.left.minPrice == 10
        assert root.right.start == 5
        assert root.right.end == 6
        assert root.right.minPrice == 10

    def test_insert_8(self):
        tree = IntervalTree()
        root = TreeNode(3, 5, 7)
        root = tree.insert(root, Interval(3, 4, 10))
        assert root.start == 3
        assert root.end == 5
        assert root.minPrice == 7

    def test_insert_9(self):
        tree = IntervalTree()
        root = TreeNode(3, 5, 7)
        root = tree.insert(root, Interval(3, 5, 10))
        assert root.start == 3
        assert root.end == 5
        assert root.minPrice == 7

    def test_insert_10(self):
        tree = IntervalTree()
        root = TreeNode(3, 5, 7)
        root = tree.insert(root, Interval(3, 6, 10))
        assert root.start == 3
        assert root.end == 5
        assert root.minPrice == 7
        assert root.right.start == 5
        assert root.right.end == 6
        assert root.right.minPrice == 10

    def test_insert_11(self):
        tree = IntervalTree()
        root = TreeNode(3, 5, 7)
        root = tree.insert(root, Interval(3, 6, 6))
        assert root.start == 3
        assert root.end == 5
        assert root.minPrice == 6
        assert root.right.start == 5
        assert root.right.end == 6
        assert root.right.minPrice == 6

    def test_insert_12(self):
        tree = IntervalTree()
        root = TreeNode(3, 6, 7)
        root = tree.insert(root, Interval(4, 5, 6))
        assert root.start == 4
        assert root.end == 5
        assert root.minPrice == 6
        assert root.left.start == 3
        assert root.left.end == 4
        assert root.left.minPrice == 7
        assert root.right.start == 5
        assert root.right.end == 6
        assert root.right.minPrice == 7

    def test_insert_13(self):
        tree = IntervalTree()
        root = TreeNode(3, 6, 7)
        root = tree.insert(root, Interval(4, 6, 6))
        assert root.start == 3
        assert root.end == 4
        assert root.minPrice == 7
        assert root.right.start == 4
        assert root.right.end == 6
        assert root.right.minPrice == 6

    def test_insert_14(self):
        tree = IntervalTree()
        root = TreeNode(3, 6, 7)
        root = tree.insert(root, Interval(4, 7, 6))
        assert root.start == 3
        assert root.end == 4
        assert root.minPrice == 7
        assert root.right.start == 4
        assert root.right.end == 7
        assert root.right.minPrice == 6

    def test_insert_15(self):
        tree = IntervalTree()
        root = TreeNode(3, 6, 7)
        root = tree.insert(root, Interval(6, 7, 6))
        assert root.start == 3
        assert root.end == 6
        assert root.minPrice == 7
        assert root.right.start == 6
        assert root.right.end == 7
        assert root.right.minPrice == 6

    # -----------------------------------------
    # Test Insert Multiple Nodes
    # -----------------------------------------

    def test_insert_multiple(self):
        tree = IntervalTree()
        root = TreeNode(3, 6, 7)
        root = tree.insert(root, Interval(1, 5, 3))
        root = tree.insert(root, Interval(4, 7, 6))
        root = tree.insert(root, Interval(2, 9, 2))
        tree.inorder(root)
        assert root.start == 5
        assert root.end == 6
        assert root.minPrice == 2
        assert root.left.start == 1
        assert root.left.end == 2
        assert root.left.minPrice == 3
        assert root.left.right.start == 2
        assert root.left.right.end == 5
        assert root.left.right.minPrice == 2
        assert root.right.start == 6
        assert root.right.end == 7
        assert root.right.minPrice == 2
        assert root.right.right.start == 7
        assert root.right.right.end == 9
        assert root.right.right.minPrice == 2


if __name__ == '__main__':
    unittest.main()